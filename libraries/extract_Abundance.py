import os

cwd=os.getcwd()

taxa={}

F=[i for i in os.listdir(cwd+"/output3") if i.split(".")[-1]=="txt"]

for myfile in F:
    f=open(cwd+"/output3/"+myfile,"r")
    f.readline()
    for line in f:
        line=line.strip()
        line=line.split("\t")
        if line[0] not in taxa:
            taxa[line[0]]=[0]*len(F)
        else:pass
        taxa[line[0]][F.index(myfile)]+=float(line[1])

o=open(cwd+"/Combined_Abundance.txt","w+")
o.write("TaxaIDs\t"+"\t".join(F)+"\n")
for i in taxa:
    o.write(i+"\t"+"\t".join([str(xx) for xx in taxa[i]])+"\n")
o.close()
