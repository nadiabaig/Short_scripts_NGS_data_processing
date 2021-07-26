with open ("Merged.vcf") as f1:
            standard_nt = ['A', 'C', 'G', 'T']
            indels=[]
            values_matrix=[]
            for i in f1:
                if i.startswith('#'):
                        continue
                else:
                    line = i.strip().split()
                    line[7]='.'
                    line[8]=''
                    ref = line[3]
                    alt = line[4]
                    if len(ref) > 1 or len(alt) > 1:
                        indels.append(i)
                    elif ref not in standard_nt or alt not in standard_nt:
                            print ('only accept valid nucleotide\n')
                            continue
                    else:
                        part1 = '\t'.join(line[0:5])
                        sample_gt = []
                        for gt in line[9:]:
                                gt = gt.split(':')[0]
                                if gt == '0/0':
                                    letter = ref*4
                                elif gt == '0/1':  #incase you have diploid samples in your vcf
                                    letter = ref*2+alt*2
                                elif gt == '1/1':
                                    letter = alt*4
                                elif gt=='0/0/0/0':
                                    letter=ref*4
                                elif gt=="1/1/1/1":
                                    letter=alt*4
                                elif gt=='0/0/1/1':
                                    letter=ref*2+alt*2
                                elif gt=="0/0/0/1":
                                    letter=ref*3+alt
                                elif gt=="0/1/1/1":
                                    letter=ref+alt*3
                                else:
                                    letter = 'na'
                                sample_gt.append(letter)
                        sample_gt = '\t'.join(sample_gt)
                        m = part1+'\t'+sample_gt
                        values_matrix.append(m)
#print(values_matrix[2])
value1= 'key1'
dict_with_lists = {}
dict_with_lists[value1]=['CHR','POS','ID','REF','ALT','s1','s2','s3','s4','s5','s6','s7','s8','s9','s10']  #change this with your sample names

with open("snp_Matrix.txt","w") as file:##add header info tomorrow
    file.writelines('\t'.join(values)+'\n' for values in dict_with_lists.values())
    for line in values_matrix:
        for l in line:
            file.write(str(l))
        file.write("\n")
