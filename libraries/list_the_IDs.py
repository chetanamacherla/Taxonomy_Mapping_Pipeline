import os

cwd=os.getcwd()
if not os.path.isdir(cwd+"/output1"):
		os.mkdir(cwd+"/output1")
for myfile in [i for i in os.listdir(cwd+"/output") if i.split(".")[-1]=="txt"]:
	f=open(cwd+"/output/"+myfile,"r")
	output=open(cwd+"/output1/"+myfile.replace("combine__","").replace(".fasta_",""),"w+")
	for line in f:
		line=line.split("\t")
		line=line[1].split(".p")
		line=line[0].split("|")
		line=line[1].split(".")
		output.write(line[0]+"\n")
	output.close()
	f.close()

	
