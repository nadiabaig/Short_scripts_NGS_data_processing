## Note: it works when your vcf has no header
#!/bin/bash


#PBS -l select=1:ncpus=1:mem=4G:arch=skylake
#PBS -l walltime=35:00:00
#PBS -A  "your-project"

module load bcftools/1.10.2

cd $PBS_O_WORKDIR
path="/path_to_your_files/.."

for i in $(ls $path/*.csv_f.txt)
do
time shuf -n 10000 ${i} > ${i}_random.txt
done

