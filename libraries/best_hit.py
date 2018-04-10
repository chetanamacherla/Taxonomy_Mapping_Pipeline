import os


cwd=os.getcwd()
def get_best(filename):
    f=open(filename)
    if not os.path.isdir(cwd+"/output"):
        os.mkdir(cwd+"/output")
    o=open("output/"+filename,"w+")
    line=f.readline()
    o.write(line)

    temp=line.split("\t")[0]
    temp_e=float(line.split("\t")[-2])
    c=1

    for i in f:
        line=i
        i=i.split("\t")

        if temp!=i[0]:
            o.write(line)
            temp_e=float(i[-2])
            
        else:
            if float(i[-2])==temp_e:
                o.write(line)

        temp=i[0]

    f.close()
    o.close()

for myfile in [i for i in os.listdir(cwd) if i.split(".")[-1]=="txt" and float(os.path.getsize(i))!=0]:
    #print myfile
    get_best(myfile)
