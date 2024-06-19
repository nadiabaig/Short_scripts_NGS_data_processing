

for i in $(ls Biallelic_*)
do
#       bcftools view --max-alleles 2 ${i} > Biallelic_${i}.vcf
#done


bcftools view -e 'INFO/TYPE="complex"' -o Biallelic_${i}_no_complex.vcf.gz.vcf ${i}
done
./biallelic.sh 
