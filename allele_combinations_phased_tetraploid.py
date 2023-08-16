def generate_allele_combinations():
    alleles = ['0', '1']
    combinations = []

    for a in alleles:
        for b in alleles:
            for c in alleles:
                for d in alleles:
                    combination = f"{a}/{b}/{c}/{d}"
                    combinations.append(combination)

    return combinations

if __name__ == "__main__":
    allele_combinations = generate_allele_combinations()

    for index, combination in enumerate(allele_combinations, start=1):
        print(f"{index}. {combination}")
