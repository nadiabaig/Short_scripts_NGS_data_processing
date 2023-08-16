 #CHROM  POS REF ALT 001 002 S003 004 005  \
 4   56   A   G       AGAG       AGAG       AGAG       AGAG       AGAG   
 4   78  GG  AT       TTGG          .          .          .          .   
 4  167   A   T       ATAT       TATA       ATAT       ATAT       ATAT

import pandas as pd

# Example DataFrame
data = {'chr': ['chr1', 'chr2'],
        'pos': [345, 456],
        '003': ['GGGT', 'CCCA'],
        '004': ['CCGT', 'AAAA']}

df = pd.DataFrame(data)

# Initialize an empty dictionary to store the results for each column
result_dict = {}

# Get the maximum length of the strings in all specified columns
max_length = max(max(df[col].apply(len)) for col in df.columns[2:])

# Iterate through the specified columns
for col in df.columns[2:]:
    result_list = []

    # Iterate through the DataFrame rows
    for i in range(max_length):
        values = [row[col][i] if len(row[col]) > i else '' for index, row in df.iterrows()]
        result_list.append(''.join(values))

    result_dict[col] = result_list

print(result_dict)
