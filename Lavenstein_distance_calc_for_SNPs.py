import pandas as pd

read your snp data 
r11=pd.read_csv('SNP_alleles.csv',sep="\t")
# Create a list of all the column names
column_names = list(r11.columns)

# Create an empty DataFrame to store the results
results = pd.DataFrame(columns=['Column 1', 'Column 2', 'Distance'])

# Define a custom function to calculate the Levenshtein distance between two columns
def levenshtein_distance(col1, col2):
  distance = 0
  for i, j in zip(col1, col2):
    if i == j:   #in lavenstein to get difference we use if i!=j but I calcuated similarity and used ==
      distance += 1
  return distance

# Iterate over all possible combinations of columns
for i, col1 in enumerate(column_names):
  for j, col2 in enumerate(column_names):
    if i < j:
      # Calculate the distance between the two columns
      distance = levenshtein_distance(r11[col1], r11[col2])
      # Store the result in the results DataFrame
      results = results.append({'Column 1': col1, 'Column 2': col2, 'Distance': distance}, ignore_index=True)


# Print the results
res2=pd.DataFrame(results) 
res2['Similarity']=(res2['Distance']/585044)*100
print('Average similarity based on lavenstein distance is :',res2['Similarity'].mean())
print('Max similarity based on lavenstein distance is :',res2.max())
print('Min similarity based on lavenstein distance is :',res2.min())

