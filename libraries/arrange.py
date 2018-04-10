import os

cwd=os.getcwd()
if not os.path.isdir(cwd+"/output3"):
		os.mkdir(cwd+"/output3")


for myfile in [i for i in os.listdir(cwd+"/output2") if i.split(".")[-1]=="txt"]:
	f=open(cwd+"/output2/"+myfile,"r")
	o=open(cwd+"/output3/"+myfile.replace("",""), "w+")
	for line in f:
		line=line.strip()
		line=line.split(" ")
		o.write(line[1]+"\t"+line[0]+"\n")
	o.close()
