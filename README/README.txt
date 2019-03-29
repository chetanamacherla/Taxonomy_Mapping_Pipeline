#### TaxonMap (Taxa Mapping) - README text file####


Input file format - The Input file to this parser should be the out files from superfocus with a .m8 extension. You can give how many ever files as an input to this parser. You just need to have all the input files, python script(Mapping_Taxa.py) and the libraries in one directory.
Output file format - The output would be an excel file with all the TaxaID mapped to the lineage (Kingdom to species level) followed by their abundances and relative abundance across all the input files  


Dependencies : Python 2.7 , Taxonkit- v0.1.7 (has locally been installed on palpatine)


Little insight into taxonkit and things to do even before we run the parser script:

This parser uses Taxonkit (NCBI Taxonomy Toolkit) to map the Tax-IDs (which are usually a part of Seed figfam ID) to their lineage.

->So this software uses the nodes.dmp and names.dmp files from the NCBI-Taxonomy as refernce files to map the Taxa to Lineage.

->Please download and uncompress the files from ftp://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz
  >to download use the command: wget ftp://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz
  >to uncompress use the command: tar -xvzf taxdump.tar.gz

->Make a directory in your home directory using command : mkdir .taxonkit and copy the names.dmp and nodes.dmp to it
  >command : cp names.dmp nodes.dmp /home/user/.taxonkit   For example: cp names.dmp nodes.dmp /home/chetana/.taxonkit
  (Note: the period before the directory name is a must, ls hides such files starting with period and these can only be seen when ls -a command is used. Its usually hidden because we dont want to make any changes to it and shell wildcards like '*' dont include such files or directories.)

->Just to verify, now we can ls into .taxonkit to see if the files are copied to the directory. Once it's done.

->Once we have the output files from superfocus (with .m8 extension), have these files, the Mapping_Taxa.py script and the libraries in a directory.


USAGE: nohup python Mapping_Taxa.py 

(nohup would run the process in background and not kill the process. Now we can close the window and open another terminal and carry out work on terminal)

To see if the process is done use top.
Once it's done a file named Combined_Taxa.xls would be created in the same directory where you run the script. The file should have the results

 
