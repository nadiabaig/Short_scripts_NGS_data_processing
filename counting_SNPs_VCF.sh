#!/bin/bash

#PBS -l select=1:ncpus=1:mem=1G
#PBS -l walltime=1:00:00
#PBS -A  "your-project"

cd $PBS_O_WORKDIR

for i in $(ls *.vcf)
do
grep -v "^#" ${i}  | cut -f 1 | sort | uniq -c > ${i}.count
done
