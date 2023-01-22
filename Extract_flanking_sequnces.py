# my_package/__init__.py
from .vcf_parser import extract_sequences

# my_package/vcf_parser.py
import pysam

def extract_sequences(vcf_file, genome_file, flank):
    vcf = pysam.VariantFile(vcf_file)
    genome = pysam.FastaFile(genome_file)
    with open("Sequences_35bp.txt", "w") as f:
        for record in vcf:
            seq = genome.fetch(record.chrom, record.pos-1-flank, record.pos-1+len(record.ref)+flank)
            t=(seq, record.chrom, str(record.pos), record.id, record.ref, record.alts[0])
            seq,chr,pos,id,ref,alt=t
            sequence='{}        [{}/{}] {}'.format(seq[:flank],ref,alt, seq[flank+len(ref):])
            line='{}\t{}\t{}\t{}'.format(chr, pos, id, sequence)
            f.write(line+'\n')
 #use this package via 
pip install my_package
from my_package import extract_sequences
extract_sequences("Final_bin_var_selected_cgn18.vcf", "Agria_assembly_final_2020_21_08.fasta", 35)
