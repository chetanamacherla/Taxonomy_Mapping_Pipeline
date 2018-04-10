import os


cwd=os.getcwd()

def removeComments(filename):

    f=open(filename)
    o=open(filename.replace(".m8",".txt"),"w+")
    for line in f:
        if not line.lstrip().startswith("#"):
            o.write(line)

    f.close()
    o.close()

for myfile in [i for i in os.listdir(cwd) if i.split(".")[-1]=="m8" and float(os.path.getsize(i))!=0]:
    #print myfile
    removeComments(myfile)
