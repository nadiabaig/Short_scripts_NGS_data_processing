sort ref_pos2.txt | uniq -d

##finding difference in two files.. it checks rows
diff -a --suppress-common-lines -y a.txt b.txt

