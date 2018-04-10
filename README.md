# Taxonomy_Mapping_Pipeline 

This tool is a set of python scripts that are called in sequential order when we run the main script which is Mapping_Taxa.py. The initial script extracts the NCBI Taxonomy ID from SEED identifiers for each metagenome and then calculates the abundance and relative abundance of  TaxaID in each metagenome and just considers the unique TaxaID across all the samples/metagenomes and puts it into an excel sheet with its corresponding abundance and relative abundance. The taxonomy/Lineage information is then extracted from NCBI using a bioinformatics tool Taxonkit (2) and mapped to TaxaID. Please find more instructions of how to run this tool and the dependencies it requires in the README folder.


1.  http://www.theseed.org/wiki/Glossary#Linking_to_the_SEED
2. http://bioinf.shenwei.me/taxonkit/
