import os

cwd=os.getcwd()

if not os.path.isdir(cwd+"/output2"):
        os.mkdir(cwd+"/output2")

for myfile in [i for i in os.listdir(cwd+"/output1") if i.split(".")[-1]=="txt"]:
	os.system("sort -n "+cwd+"/output1/"+myfile+" | uniq -c >>  "+cwd+"/output2/"+myfile)

