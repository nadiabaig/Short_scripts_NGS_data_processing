#vcf allele conversions --fix this first

with open ("Intermediate_vcf.txt") as f1:
            lines = f1.readlines()[1:]
            #standard_nt = ['A', 'C', 'G', 'T']
            #indels=[]
            values_matrix=[]
            for i in lines:
                if i.startswith('Chr     Pos'):
                        continue
                else:
                    line = i.strip().split()
                    ref=line[2]
                    alt=line[3]
                    part1='\t'.join(line[0:5])  #part before ref and alt
                    sample_gt=[]

                    for gt in line[4:]:
                        if gt == '0/0/0/0':
                                    letter = ref*4
                        elif gt == '0/0/1/1': 
                                    letter = ref*2+alt*2
                        elif gt == '0/1/1/1':
                                    letter = ref+alt*3
                        elif gt=='0/0/0/1':
                                    letter=ref*3+alt
                        elif gt=="1/1/1/1":
                                    letter=alt*4
                        else:
                                    letter = 'na'
                        sample_gt.append(letter)
                    sample_gt = '\t'.join(sample_gt)
                    m = part1+'\t'+sample_gt
                    values_matrix.append(m)

value1= 'key1'
dict_with_lists = {}

dict_with_lists[value1]=['CHROM', 'POS', 'REF', 'ALT', 'COMB', 'ADRETTA', 'AGRIATETRAPLOID', 'ALBATRS', 'ALLIANS', 'ALTUS', 'AMBITION', 'ATLNTIC', 'ATZIMBA', 'BELANA', 'BINTJE', 'BNA_1', 'BNA_2', 'BNA_3', 'BNA_4', 'BNA5', 'CARA', 'CELTANE', 'CHARLTE', 'CHERIE', 'COLOMBA', 'DARK', 'DESIREE', 'DONATA', 'EARYRSE', 'EDISON', 'EUROGRAN', 'EUROPRIM', 'FELSINA', 'FLAVA', 'FONTANE', 'GALA', 'GLADITOR', 'GRANOLA', 'HARPUN', 'HERMES', 'INNOVAT', 'JELLY', 'JUKIJIRO', 'KARELIA', 'KAROLIN', 'KATHADIN', 'KENN', 'KINGRUST', 'KOLIBRI', 'KRONE', 'KUBA', 'KURAS', 'LADYROSE', 'LAURA', 'LEYLA', 'LILLY', 'MARABEL', 'MARSPIPR', 'NATALIA', 'NEVSKY', 'NICOLA', 'ODYSSEUS', 'OLYMPUS', 'ONA', 'OTOLIA', 'PENTDELL', 'PIROL', 'PREMIERRUSSET', 'PRINCESS', 'QUADRIGA', 'QUARTA_FILES', 'RECORD', 'REGINA', 'RODE_EST', 'ROOSTER', 'ROSARA', 'RSETBUR', 'RUDOLPH', 'S13_017', 'S14214', 'S14317_1', 'S14_9122', 'S5061', 'S5089', 'S5202', 'S5220A', 'S5342', 'SASKIA', 'SEMLO', 'SERESTA', 'SHC909', 'SHEPODY', 'SKAWA', 'SNOWDEN', 'SOLIST', 'SPUNTA', 'TALENT', 'TOYOSHI', 'UDACHA', 'VELOX', 'VERDI', 'VITABLLA', 'VR808', 'YANGANA', 'ZORBA']
with open("06_vcf_calls.txt","w") as file:
    file.writelines('\t'.join(values)+'\n' for values in dict_with_lists.values())
    for line in values_matrix:
        for l in line:
            file.write(str(l))
        file.write("\n")
