#!/bin/bash

#PBS -l select=1:ncpus=1:mem=12G
#PBS -l walltime=9:00:00
#PBS -A  "your project"

module load bcftools/1.10.2
cd $PBS_O_WORKDIR

bcftools filter -i "TYPE='snp'" Tetraploids_raw.vcf.maf | wc -l > snp.txt
bcftools filter -i "TYPE='ins'" Tetraploids_raw.vcf.maf | wc -l > ins.txt
bcftools filter -i "TYPE='del'" Tetraploids_raw.vcf.maf | wc -l > del.txt
bcftools filter -i "TYPE='mnp'" Tetraploids_raw.vcf.maf | wc -l > mnp.txt
bcftools filter -i "TYPE='complex'" Tetraploids_raw.vcf.maf | wc -l > complex.txt
