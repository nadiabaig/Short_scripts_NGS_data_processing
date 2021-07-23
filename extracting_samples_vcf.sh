
#!/bin/bash


#PBS -l select=1:ncpus=1:mem=150G:arch=skylake
#PBS -l walltime=50:00:00
#PBS -A  "PotatoTool-BI"

cd $PBS_O_WORKDIR
##make a list of samples to be extracted using
vim adt.txt
##add Adretta into adt.txt and save it.

bcftools view -S adt.txt All_samples.vcf > adretta.vcf
