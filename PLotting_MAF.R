
library(ggplot2)
#install.packages("ggrepel")
#library(ggrepel)

getwd()
setwd("/home/baign")
pop_t=read.csv("mafb.txt")
names(pop_t)[1] <- "MAF"
#head(pop_t)
postscript("maf_before.ps")
#png("before_maf.png",width=6,height=6,units="in",res=1200)
hist(pop_t$MAF, main="MAF distribution in tetraploids",
     xlab="MAF",
     xlim=c(0,0.5),
     col="lightgrey"
     )
dev.off()
