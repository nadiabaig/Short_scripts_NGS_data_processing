 #CHROM  POS REF ALT 001 002 S003 004 005  \
 4   56   A   G       AGAG       AGAG       AGAG       AGAG       AGAG   
 4   78  GG  AT       TTGG          .          .          .          .   
 4  167   A   T       ATAT       TATA       ATAT       ATAT       ATAT

import pandas as pd

# Example DataFrame
data = {'chr': ['chr1', 'chr2'],
        'pos': [345, 456],
        '002': ['AAAT', 'TTAA']}

df = pd.DataFrame(data)

# Initialize an empty list to store the results
result_list = []

# Get the maximum length of the strings
max_length = max(df['002'].apply(len))

# Iterate through the DataFrame rows
for i in range(max_length):
    values = [row['002'][i] if len(row['002']) > i else '' for index, row in df.iterrows()]
    result_list.append(''.join(values))

print(result_list)
