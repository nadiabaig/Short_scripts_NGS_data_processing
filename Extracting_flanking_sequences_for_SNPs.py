
from __future__ import print_function
import pysam

vcf = pysam.VariantFile("Final_bin_var_selected_cgn18.vcf")

genome = pysam.FastaFile("Agria_assembly_final_2020_21_08.fasta")

flank=35  #you can change it as per your requirement


with open("Sequences_35bp.txt", "w") as f:

        for record in vcf:

        
            seq = genome.fetch(record.chrom, record.pos-1-flank, record.pos-1+len(record.ref)+flank)

            t=(seq, record.chrom, str(record.pos), record.id, record.ref, record.alts[0])

            seq,chr,pos,id,ref,alt=t

            sequence='{}        [{}/{}] {}'.format(seq[:flank],ref,alt, seq[flank+len(ref):])

            line='{}\t{}\t{}\t{}'.format(chr, pos, id, sequence)

            f.write(line+'\n')
