import os

cwd=os.getcwd()
if not os.path.isdir(cwd+"/Relative"):
        os.mkdir(cwd+"/Relative")

for myfile in [i for i in os.listdir(cwd+"/output3") if i.split(".")[-1]=="txt"]:
           output = open(cwd+"/Relative/"+myfile, 'w+')
           numbers = []
           with open(cwd+"/output3/"+myfile,'r') as file1:
                      for f in file1:
                                 q1 = f.strip()
                                 q2 = q1.split('\t')
                                 numbers.append(int(q2[1]))
           total = sum(numbers)
           
           with open(cwd+"/output3/"+myfile,'r') as file2:
                      for out in file2:
                                 r1 = out.strip()
                                 r2 = r1.split('\t')
                                 tab_2 =float(r2[1])/total
                                 tab_1 = int(r2[0])
                                 output.write(str(tab_1)+'\t'+str(tab_2)+'\n')
           output.close() 
                                 
                                 

