#!/bin/bash
tool=/1data/Nadia/Project1/src/bin
path=/1data/Nadia/Project1y/05_Filtered_VCFS/01_tetraploids/per_sample_vcf
export PATH=$PATH:/1data/Nadia/Project1/src/bin

for i in $(ls *.vcf)
do
vcf2bed --snvs < $path/${i} > ${i}_variants.snvs.bed     #snp
vcf2bed --insertions < $path/${i} > ${i}_variants.ins.bed    #insertions
vcf2bed --deletions < $path/${i} > ${i}_variants.del.bed     #deletions
done

wait

for j in $(ls *.snvs.bed)
do
for chr in `bedextract --list-chr ${j}`; 
do   
        echo $chr >> ${j}_snp.txt; 
        bedextract $chr ${j} | wc -l >> ${j}_snp.txt ;
done  ##for snps
done
wait
##now extract count of insertions

for j in $(ls *.ins.bed)
do
for chr in `bedextract --list-chr ${j}`;
do
        echo $chr >> ${j}_ins.txt;
        bedextract $chr ${j} | wc -l >> ${j}_ins.txt ;
done  ##for ins
done
wait

for j in $(ls *.del.bed)
do
for chr in `bedextract --list-chr ${j}`;
do
        echo $chr >> ${j}_del.txt;
        bedextract $chr ${j} | wc -l >> ${j}_del.txt ;
done  ##fordeletions
done


