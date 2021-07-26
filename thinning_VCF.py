####Filtering on position per chromosome ####

import vcf     # pip3 install --user  PyVCF


# A)  Read input and save positions to posis
posis = []

vcf_input = vcf.Reader(open(f'Chr2_filtered.vcf', 'r')) #your vcf

for record in vcf_input:
    posis.append(record.POS)


# B) Check for neighbours in all positions. Save positions without neighbours to ids_to_keep
ids_to_keep = []

for i, pos in enumerate(posis):

    try: # Just in case there is an error
        if (pos +35 > posis[i+1]): pass   #you can change the distance here.
        elif(pos - 35 < posis[i-1]): pass
        else: ids_to_keep.append(i)
    except: pass



# C) prepare input and output again
vcf_output = vcf.Writer(open('Chr2_filtered_pos.vcf', 'w'), vcf_input)
vcf_input = vcf.Reader(open(f'Chr2_filtered.vcf', 'r'))


# counter updates with each input record read
record_id = 0

# D) Write record if id was kept in part B
for record in vcf_input:
    if record_id in ids_to_keep:
        vcf_output.write_record(record)

    record_id += 1

