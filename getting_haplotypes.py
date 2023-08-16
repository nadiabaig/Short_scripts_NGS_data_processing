 #CHROM  POS REF ALT 001 002 S003 004 005  \
 4   56   A   G       AGAG       AGAG       AGAG       AGAG       AGAG   
 4   78  GG  AT       TTGG          .          .          .          .   
 4  167   A   T       ATAT       TATA       ATAT       ATAT       ATAT

def extract_haplotypes(genotype):
    haplotypes = set()
    alleles = genotype.split('/')
    for hap1 in alleles:
        for hap2 in alleles:
            haplotypes.add(hap1 + '.' + hap2)
    return haplotypes

vcf_data = [
    ("4", 56, "A", "G", "AGAG", "AGAG", "AGAG", "AGAG", "AGAG"),
    ("4", 78, "GG", "AT", "TTGG", ".", ".", ".", "."),
    ("4", 167, "A", "T", "ATAT", "TATA", "ATAT", "ATAT", "ATAT")
]

haplotypes_by_genotype = {}

for entry in vcf_data:
    chrom, pos, ref, alt, *genotypes = entry
    for i, genotype in enumerate(genotypes):
        haplotypes = extract_haplotypes(genotype)
        haplotypes_by_genotype[f"{chrom}_{pos}_{i + 1}"] = haplotypes

output_file = "haplotypes.txt"
with open(output_file, "w") as f:
    for genotype, haplotypes in haplotypes_by_genotype.items():
        f.write(f"{genotype}: {', '.join(haplotypes)}\n")

print(f"Haplotypes written to {output_file}")




