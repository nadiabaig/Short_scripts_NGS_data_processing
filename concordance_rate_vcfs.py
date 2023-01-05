import vcf

def calculate_concordance(vcf_file_1, vcf_file_2):
    # Open the VCF files
    vcf_reader_1 = vcf.Reader(open(vcf_file_1, 'r'))
    vcf_reader_2 = vcf.Reader(open(vcf_file_2, 'r'))

    # Initialize counters for concordant and discordant genotypes
    concordant_count = 0
    discordant_count = 0

    # Iterate over the genotypes in the first VCF file
    for record_1 in vcf_reader_1:
        # Find the corresponding genotype in the second VCF file
        record_2 = vcf_reader_2.fetch(record_1.CHROM, record_1.POS)

        # Compare the genotypes
        if record_1.samples[0]['GT'] == record_2.samples[0]['GT']:
            concordant_count += 1
        else:
            discordant_count += 1

    # Calculate the concordance rate
    concordance_rate = concordant_count / (concordant_count + discordant_count)
    return concordance_rate
