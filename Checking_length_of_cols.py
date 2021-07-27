##checking length of rows
import pandas as pd
import numpy as np
df=pd.read_csv("test.txt",sep="\t")
df['length']=len(df.columns)
list1=[]
for i in df['length']:
    if i <113:
        list1.append(df)
t=pd.DataFrame(np.concatenate(list1))
t.to_csv("length_check.txt",sep="\t",index=False) 
