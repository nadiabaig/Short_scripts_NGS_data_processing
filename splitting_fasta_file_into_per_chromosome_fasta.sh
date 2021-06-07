#!/bin/bash

#PBS -l select=1:ncpus=1:mem=3G

#PBS -l walltime=2:00:00
#PBS -A  "yur-project"

module load Java/1.8.0_151
module load SamTools/1.6
cd $PBS_O_WORKDIR
while read line ; do
  if [ ${line:0:1} == ">" ] ; then
    filename=$(echo "$line" | cut -d ":" -f1 | tr -d ">")
    touch ./"$filename".fasta
    echo "$line" >> ./"${filename}".fasta
  else
    echo "$line" >> ./"${filename}".fasta
  fi
done < $1
