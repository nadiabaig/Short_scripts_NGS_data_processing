##filtering monomorphic
##Author: Nadia Baig #################################################
##Institute of Quantitative genetics and genomics for plants-QGGP   ##
######################################################################
import pandas as pd
import statistics
import math

l2=pd.read_csv("chr01.txt",sep="\t")

l2['AAAA'] = (l2.select_dtypes(include=[object]) == '0/0/0/0').sum(axis=1)
l2['BBBB']=(l2.select_dtypes(include=[object])=='1/1/1/1').sum(axis=1)
l2['Missing']=(l2.select_dtypes(include=[object])=='./././.').sum(axis=1)
l2['AA'] = (l2.select_dtypes(include=[object]) == '0/0').sum(axis=1)
l2['BB'] = (l2.select_dtypes(include=[object]) == '1/1').sum(axis=1)
l2['Sum_AAAA']=l2['AAAA']+l2['AA']+l2['Missing']
l2['Sum_BBBB']=l2['BBBB']+l2['BB']+l2['Missing']
l3 = l2[l2['Sum_AAAA']<108]
l4=l3[l3['Sum_BBBB']<108]
l5=l4[l4['Missing']<=20]
####Now dropping last cols which contains values
l6=l5.iloc[:, :-7]
l6.to_csv("filtered.vcf",sep="\t",index=False)
