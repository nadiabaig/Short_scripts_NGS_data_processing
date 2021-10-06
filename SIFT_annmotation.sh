#!/bin/bash
#PBS -l select=1:ncpus=1:mem=10gb
#PBS -l walltime=40:00:00
#PBS -A "yourprojectName_HPC"

cd $PBS_O_WORKDIR

sample="Tetraploid"
input_vcf="/gpfs/project/baign/SIFT_tetraploids/All_merged_sorted.vcf"

for chrom in chr01 chr02 chr03 chr04 chr05 chr06 chr07 chr08 chr09 chr10 chr11 chr12 chrun
do
        java -jar /gpfs/project/projects/qggp/src/SIFT4G_Annotator_v2.4.jar -c -i ${input_vcf} -d /gpfs/project/projects/qggp/Potatodenovo/experiments/deleterious_alleles/SIFT4G_${chrom}/Agria_version_2020 -r ${sample}_${chrom}_annotated -t
done
