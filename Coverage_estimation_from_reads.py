genome=89719359+52458522+61672818+73201088+56731602+55985673+53532588+63071485+73873122+57411799+55350225+57049570+68158033
#reads=coverage*genomesize/read_length
#coverage=read_length*total no on reads/genome_size
print('Genome length in bp potato:',genome)
cov=30
read_length=150*2-30 #paired end read ,15 is the barcode size
reads=round((cov*genome)/read_length)
coverage=round((read_length*reads)/genome)
print('reads needed to get 30x coverage:', reads)
print('coverage of',reads,'is',coverage,'considering',genome ,'bp potato genome length')
