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
