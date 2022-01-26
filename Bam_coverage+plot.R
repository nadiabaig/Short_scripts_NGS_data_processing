#getting per base coverage of a bam file
##tot=$(samtools view -H possorted_bam.bam | grep -P '^@SQ' | cut -f 3 -d ':' | awk '{sum+=$1} END {print sum}')

#samtools depth possorted_bam.bam > all.cov
#awk '$1 == "Chr01" {print $0}' 1.cov > Chr1.cov  #for chr1

##checking total coverage
#sum=$(awk '{sum+=$3} END {print sum}' 1.cov ); echo $sum

##avg coverage
#avg=$(echo "$sum/$tot" | bc -l)

##PLotting in R
library(reshape)
setwd('/home/baign/Desktop')
chr1=read.table('1.cov',header = FALSE, sep="\t",na.strings = NA, dec = '.',strip.white = TRUE)
chr1=rename(chr1,c(V1="Chr",V2="Position",V3="Depth"))
plot(chr1$Position,chr1$Depth)

##get a cleaner view of the graph
library(lattice, pos=10) 
xyplot(Depth ~ Position, type="p", pch=16, auto.key=list(border=TRUE), par.settings=simpleTheme(pch=16), scales=list(x=list(relation='same'), y=list(relation='same')), data=chr1)

##checking depth and other statitistics of your vcf file

##plotting vcf stats
library('vcfR')
vcf=read.vcfR('Filtered_1mb.vcf',verbose = FALSE)
dna= ape::read.dna('Chr01_1mb.fa',format ="fasta")

##create chromR object
chrom<- create.chromR(name="Chr01", vcf=vcf, seq=dna, verbose=TRUE)
#visualizing chrom object
chrom <- proc.chromR(chrom, verbose=FALSE, win.size=1e0)
chromoqc(chrom, dp.alpha = 22)

###plot only depth
dp <- extract.gt(vcf, element = "DP", as.numeric=TRUE)
##base plot

boxplot(dp, col=2:8, las=3)
title(ylab = "Depth (DP)")
