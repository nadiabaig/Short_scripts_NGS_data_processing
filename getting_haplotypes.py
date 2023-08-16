def create_dummy_phased_vcf():
    header = """\
##fileformat=VCFv4.2
##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotype">
#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  Sample1 Sample2
"""

    variants = [
        ("chr1", 1000, "rs123", "A", "T", ".", "PASS", ".", "GT", "0|1", "1|0"),
        ("chr1", 2000, "rs456", "C", "G", ".", "PASS", ".", "GT", "0/0", "1/1"),
        ("chr2", 3000, "rs789", "G", "T", ".", "PASS", ".", "GT", "0|1", "1|0"),
    ]

    vcf_lines = [header]

    for variant in variants:
        chrom, pos, var_id, ref, alt, qual, filt, info, fmt, sample1, sample2 = variant
        vcf_line = f"{chrom}\t{pos}\t{var_id}\t{ref}\t{alt}\t{qual}\t{filt}\t{info}\t{fmt}\t{sample1}\t{sample2}\n"
        vcf_lines.append(vcf_line)

    return vcf_lines

if __name__ == "__main__":
    vcf_lines = create_dummy_phased_vcf()

    with open("dummy_phased.vcf", "w") as vcf_file:
        vcf_file.writelines(vcf_lines)

def get_haplotypes_from_vcf(vcf_filename):
    haplotypes = {}

    with open(vcf_filename, "r") as vcf_file:
        for line in vcf_file:
            if line.startswith("#"):
                continue  # Skip header lines

            fields = line.strip().split("\t")
            chrom, pos, var_id, ref, alt, qual, filt, info, fmt = fields[:9]
            samples = fields[9:]

            for sample_index, sample in enumerate(samples):
                sample_name = f"Sample{sample_index + 1}"
                genotype = sample.split(":")[0]

                if "|" in genotype:
                    haplotypes.setdefault(sample_name, []).append(genotype.split("|"))
                elif "/" in genotype:
                    haplotypes.setdefault(sample_name, []).append(genotype.split("/"))

    return haplotypes

if __name__ == "__main__":
    vcf_filename = "dummy_phased.vcf"
    haplotypes = get_haplotypes_from_vcf(vcf_filename)

    for sample, haplotype_list in haplotypes.items():
        print(f"Haplotypes for {sample}:")
        for index, haplotype in enumerate(haplotype_list, start=1):
            print(f"Haplotype {index}: {' '.join(haplotype)}")
