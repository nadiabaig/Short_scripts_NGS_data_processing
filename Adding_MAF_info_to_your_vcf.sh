#!/bin/bash
#PBS -l select=1:ncpus=1:mem=5G
#PBS -l walltime=28:59:00
#PBS -A yourprojectname

module load bcftools/1.10.2 
cd $PBS_O_WORKD
for i in $(ls *.vcf)
do

bcftools +fill-tags ${i} -Ov -o ${i}.gz -- -t all

done

