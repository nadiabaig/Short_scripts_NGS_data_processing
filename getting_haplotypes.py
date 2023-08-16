def create_phased_tetraploid_vcf():
    header = """\
##fileformat=VCFv4.2
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  Sample1 Sample2
"""

    variants = [
        ("chr1", 1000, "rs123", "A", "T", ".", "PASS", ".", "GT", "0|0|0|1", "0|1|1|1"),
        ("chr1", 2000, "rs456", "C", "G", ".", "PASS", ".", "GT", "0|0|1|1", "0/1|0/1"),
        ("chr2", 3000, "rs789", "G", "T", ".", "PASS", ".", "GT", "0|1|1|1", "1|0|1|0"),
    ]

    vcf_lines = [header]

    for variant in variants:
        chrom, pos, var_id, ref, alt, qual, filt, info, fmt, sample1, sample2 = variant
        vcf_line = f"{chrom}\t{pos}\t{var_id}\t{ref}\t{alt}\t{qual}\t{filt}\t{info}\t{fmt}\t{sample1}\t{sample2}\n"
        vcf_lines.append(vcf_line)

    with open("phased_tetraploid.vcf", "w") as vcf_file:
        vcf_file.writelines(vcf_lines)

if __name__ == "__main__":
    create_phased_tetraploid_vcf()
    print("Created phased tetraploid VCF")

def convert_to_allele_sequences(haplotype, ref, alt):
    return [allele.replace('0', ref).replace('1', alt) for allele in haplotype]

def extract_haplotypes(vcf_filename):
    haplotypes = {}

    with open(vcf_filename, "r") as vcf_file:
        for line in vcf_file:
            if line.startswith("#"):
                continue

            fields = line.strip().split("\t")
            chrom, pos, var_id, ref, alt, qual, filt, info, fmt = fields[:9]
            samples = fields[9:]

            for sample_index, sample in enumerate(samples):
                sample_name = f"Sample{sample_index + 1}"
                genotype = sample.split(":")[0]
                haplotype = genotype.split("|")

                haplotypes.setdefault(sample_name, []).append(haplotype)

    return haplotypes

def write_haplotypes_to_file(haplotypes):
    with open("haplotypes.txt", "w") as haplotype_file:
        for sample, haplotype_list in haplotypes.items():
            haplotype_file.write(f"{sample}:\n")
            for index, haplotype in enumerate(haplotype_list, start=1):
                allele_seq = convert_to_allele_sequences(haplotype, ref_allele, alt_allele)
                haplotype_file.write(f"Haplotype {index}: {' '.join(allele_seq)}\n")

def main():
    vcf_filename = "phased_tetraploid.vcf"

    # Step 2: Convert phased SNPs to allele sequences
    ref_allele = "A"
    alt_allele = "T"
    haplotypes = extract_haplotypes(vcf_filename)

    allele_sequences = {}
    for sample, haplotype_list in haplotypes.items():
        allele_sequences[sample] = []
        for haplotype in haplotype_list:
            allele_seq = convert_to_allele_sequences(haplotype, ref_allele, alt_allele)
            allele_sequences[sample].append(allele_seq)

    print("Step 2: Converted phased SNPs to allele sequences")

    # Step 3: Get possible Haplotypes for all genes
    for sample, allele_seq_list in allele_sequences.items():
        print(f"Haplotypes for {sample}:")
        for index, allele_seq in enumerate(allele_seq_list, start=1):
            print(f"Haplotype {index}: {' '.join(allele_seq)}")

    # Step 4: Write Haplotypes under genotype names
    write_haplotypes_to_file(allele_sequences)
    print("Step 4: Wrote Haplotypes under genotype names")

if __name__ == "__main__":
    main()
