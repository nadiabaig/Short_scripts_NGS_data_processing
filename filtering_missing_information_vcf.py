
import pandas as pd
import time
start_time = time.time()
df=pd.read_csv("chr1_all_tet_filtered_final_monomorphic.vcf.header",sep='\t',error_bad_lines=False, index_col=False,skiprows=90, dtype='unicode') #skip rows is skipping header of vcf
df['Total_missing'] = (df.select_dtypes(include=[object]) == '.:.:.:.:.:.:.').sum(axis=1)
df = df[df['Total_missing'] <=20]
df['Total_missing'] = pd.to_numeric(df['Total_missing'])
df2 = df.iloc[:, :-1] #dropping last column
df2.to_csv("chr1_all_tet_filtered_final_monomorphic_nomiss_20_per.vcf",sep='\t', index=False)
#df4.to_csv('lessthan_23_miss.vcf',sep='\t', index=False)
print("--- %s seconds ---" % (time.time() - start_time))

