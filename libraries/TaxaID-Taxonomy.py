import os
cwd=os.getcwd() 

f=open(cwd+"/Combined_Abundance.txt","r")
f.readline()
o=open(cwd+"/List_Taxa.txt","w+")
list_Taxa={}
for line in f:
	line=line.strip()
	line=line.split("\t")
	list_Taxa[line[0]]=0
for i in list_Taxa:
	o.write(i+"\n")

o.close()

os.system("cat "+cwd+"/List_Taxa.txt | taxonkit lineage | taxonkit reformat --fill-miss-rank > "+cwd+"/trial.txt" )

os.system('''cat '''+cwd+'''/trial.txt | awk -F "\t" '{print $1";"$3}' | sed 's/unclassified superkingdom;unclassified phylum;unclassified class;unclassified order;unclassified family;unclassified genus;unclassified species/unclassified/' > '''+cwd+'''/Taxonomy.txt''')

f1=open(cwd+"/Taxonomy.txt","r")
o1=open(cwd+"/Taxonomy1.txt","w+")
o1.write("TaxaIDs\tKingdom\tPhylum\tClass\tOrder\tFamily\tGenus\tSpecies\n")
for line1 in f1:
	line1=line1.strip()
	line1=line1.replace(";","\t")
	o1.write(line1+"\n")

f1.close()
o1.close()

print "Done! :D"
