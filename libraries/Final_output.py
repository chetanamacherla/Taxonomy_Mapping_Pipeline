import os

cwd=os.getcwd()

os.system("sort -n -k1,1 "+cwd+"/Taxonomy1.txt > "+cwd+"/Taxonomy2.txt")

os.system("sort -n -k1,1 "+cwd+"/Combined_Abundance.txt > "+cwd+"/Combined_Abundance1.txt")

os.system("sort -n -k1,1 "+cwd+"/Combined_Relative-Abundance.txt > "+cwd+"/Combined_Relative-Abundance1.txt")

os.system("cut -f 2- "+cwd+"/Combined_Abundance1.txt > "+cwd+"/Combined_Abundance2.txt")

os.system("cut -f 2- "+cwd+"/Combined_Relative-Abundance1.txt > "+cwd+"/Combined_Relative-Abundance2.txt")

os.system("paste "+cwd+"/Taxonomy2.txt "+cwd+"/Combined_Abundance2.txt "+cwd+"/Combined_Relative-Abundance2.txt > "+cwd+"/Combined_Taxonomy.xls")