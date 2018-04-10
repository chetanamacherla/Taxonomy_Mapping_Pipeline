import os

cwd=os.getcwd()

os.system("python libraries/Remove_comments.py")

os.system("python libraries/best_hit.py")

os.system("python libraries/list_the_IDs.py")

os.system("python libraries/abundance.py")

os.system("python libraries/arrange.py")

os.system("python libraries/extract_Abundance.py")

os.system("python libraries/ToFindRelativeAbund.py")

os.system("python libraries/extract_Relative-Abun.py")

os.system("python libraries/TaxaID-Taxonomy.py")

os.system("python libraries/Final_output.py")

os.system("rm -rf "+cwd+"/output")

os.system("rm -rf "+cwd+"/output1")

os.system("rm -rf "+cwd+"/output2")

os.system("rm -rf "+cwd+"/output3")

os.system("rm -rf "+cwd+"/Relative")

os.system("rm -rf "+cwd+"/*.txt")
