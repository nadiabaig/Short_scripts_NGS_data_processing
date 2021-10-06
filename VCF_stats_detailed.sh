#!/bin/bash

#PBS -l select=1:ncpus=1:mem=18G
#PBS -l walltime=72:00:00
#PBS -A  "your_prohec_HPC"    #please skip three lines #PBS and module load if you are not using HPC cluster.. Provide the path of your installed tools


module load bcftools/1.10.2  
module load Python/3.6.5
module load R/3.6.1
cd $PBS_O_WORKDIR
infolder=$PBS_O_WORKDIR
 
# save results in the session result folder
outfolder=stats_raw
mkdir -p ${outfolder}

 
############
# aln calls
bcftools stats ${infolder}/Tetraploids_raw.vcf > \
       ${outfolder}/test.check
 
plot-vcfstats -t "NA18507_aln-calls" \
       -p ${outfolder}/chr21_aln_plots/ \
       ${outfolder}/test.check
 
 

export PATH=/home/baign/.local/bin:$PATH
export PATH=/home/baign/R/libs:$PATH
export PATH=/home/baign/PotatoTools/PhDNadia/src/R/libs/ggplot2:$PATH
#library(ggplot2)



vcfstats --vcf $p/Final_filtered_MAF_0.05_qual_20_qual_Ao_10_saf_0_MQM_MQMR.vcf  \
        --outdir $p \
        --formula 'COUNT(1) ~ CONTIG' \
        --title 'Number of variants on each chromosome' \
       
wait
vcfstats --vcf $p/CGN17881_normalized_dp15_avgdp_3sd_only_indel_snp_Qual_20_filtered_nomissing_pos_30_gc_0.3_0.7_Reheader.vcf \
        -outdir $p \
        --formula 'COUNT(1) ~ CONTIG' \
        --title 'Number of variants on each chromosome' 
        --config $p/config.toml
#####
wait
vcfstats --vcf $p/Final_filtered_MAF_0.05_qual_20_qual_Ao_10_saf_0_MQM_MQMR.vcf \
       --outdir $p \
       --formula 'COUNT(1, VARTYPE[snp]) ~ SUBST[A>T,A>G,A>C,T>A,T>G,T>C,G>A,G>T,G>C,C>A,C>T,C>G]' \
       --title 'Number of substitutions of SNPs' \
wait
##AAF on each chr
vcfstats --vcf $p/Final_filtered_MAF_0.05_qual_20_qual_Ao_10_saf_0_MQM_MQMR.vcf \
       --outdir $p \
       --formula 'AAF ~ CONTIG' \
       --title 'Allele frequency on each chromosome' \
      --figtype boxplot
wait

vcfstats --vcf $p/ CGN_18114.vcf \
      --outdir $p \
      --formula 'AAF ~ CONTIG[1,2,3,4,5,6,7,8]' \
      --title 'Allele frequency on chromosome 1 to 8' \
      --figtype density
wait
#overall freq dist
vcfstats --vcf $p/Final_filtered_MAF_0.05_qual_20_qual_Ao_10_saf_0_MQM_MQMR.vcf \
       --outdir $p \
       --formula 'AAF ~ 1' \
       --title 'Overall allele frequency distribution' \
wait
p=/home/baign/PotatoTools/new_merged_21_02_2021
#type ov var on each chr
vcfstats --vcf $p/Tetraploids_raw.vcf \
        --outdir $p \
        --title 'Types of variants on each chromosome' \
        --formula 'COUNT(1, group=VARTYPE) ~ CHROM' 
#       --title 'Types of variants on each chromosome'
