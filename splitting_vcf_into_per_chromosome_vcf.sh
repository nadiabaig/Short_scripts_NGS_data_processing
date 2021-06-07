
#!/bin/bash


#PBS -l select=1:ncpus=1:mem=6G:arch=skylake
#PBS -l walltime=10:00:00
#PBS -A  "your-project"

module load bcftools/1.10.2
cd $PBS_O_WORKDIR
VCF="Final_filtered_7_june_2021.vcf"
VCFGZ="${VCF##*/}.gz"  # get basename and add .gz compression extension

bgzip -c $VCF > $VCFGZ  #compress vcf
tabix -p vcf $VCFGZ  # index compressed vcf
tabix --list-chroms $VCFGZ > chromosomes.txt  # save all the chromosome names into a file

while IFS= read -r line; do
  tabix $VCFGZ $line > $line.vcf;
done < chromosomes.txt
