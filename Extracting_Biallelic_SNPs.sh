
#!/bin/bash

#PBS -l select=1:ncpus=1:mem=1G
#PBS -l walltime=1:00:00
#PBS -A  "your-project"


module load GATK/3.7
module load SamTools/1.6
module load Java/1.8.0_151

cd $PBS_O_WORKDIR
reference="/gpfs/..../ref.fa"  #path of your reference
for x in {GN17881,GLKS3,P3,p40,SA222_2,SA225_2}; ##your sample folder names
do
cd /gpfs/.../vcfs/raw_vcf/$x  #path to your parent folder where sample folders are created
echo "#!/bin/bash
#PBS -l select=1:ncpus=2:mem=10G
#PBS -l walltime=36:59:00
#PBS -A "your-project"

module load GATK/3.7
module load SamTools/1.6
module load Java/1.8.0_151

cd /gpfs/...../vcfs/raw_vcf/$x

for files in \$(ls *.vcf.gz)
do
java -jar /software/gatk/3.7/GenomeAnalysisTK.jar -T SelectVariants \
  -R $reference \
  -o \$files._biallelic.vcf \
  --variant \$files \
  -restrictAllelesTo BIALLELIC
done " > /gpfs/....../vcfs/raw_vcf/bi-allelic.$x.sh  #replace it with complete paths
cd /gpfs/......./vcfs/raw_vcf
qsub bi-allelic.$x.sh

done

