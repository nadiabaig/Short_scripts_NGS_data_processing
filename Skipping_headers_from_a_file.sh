


#!/bin/bash


#PBS -l select=1:ncpus=1:mem=1G:arch=skylake
#PBS -l walltime=2:00:00
#PBS -A  "your-project"

cd $PBS_O_WORKDIR

for i in $(ls *.txt)
:xq:xdo 
awk '(NR > 15)' ${i} > ${i}_p.txt #skipping 15 rows of your file
done
