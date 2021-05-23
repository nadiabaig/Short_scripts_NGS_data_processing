#!/bin/bash

#PBS -l select=1:ncpus=4:mem=35G
#PBS -l walltime=5:00:00
#PBS -A  "xyz"

cd $PBS_O_WORKDIR
#for the reads of second library
rand_tool="/gpfs/project/projects/---/src/seqtk/seqtk"
Path="/gpfs/project/projects/3665_B/" #change path as per your requirement
sample1="3665_B_run513_SI-GA-B4_S2_L006_R1_001.fastq.gz 3665_B_run513_SI-GA-B4_S2_L007_R1_001.fastq.gz 3665_B_run517_SI-GA-B4_S1_L004_R1_001.fastq.gz"

for r in $sample2; do
r1=$r
r1="${r/R1/R2}" #this will do the same for your R2_001.fastq.gz files
#echo $Path_files$sample
$rand_tool sample -s102 $Path$r 10219985 > ${r}_forward.fastq.gz  #change 10219985  this with the no. of reads you want

done

wait


