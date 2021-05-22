#!/bin/bash
#PBS -l select=1:ncpus=1:mem=5G
#PBS -l walltime=28:59:00
#PBS -A PotatoTool-BI


cd $PBS_O_WORKD

for i in $(ls *.vcf)
do

bgzip ${i}
wait

tabix -p vcf ${i}.gz
wait
### set the chromosome and region for your vcf files 
tabix ${i}.gz chr1:100-5670 > your_output.vcf  #will ectract the SNPs from specified regions for all vcfs

done

