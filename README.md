# HOMD_PICRUSt
# Dr. Alexander Alekseyenko
# Ricky Ramos

HOMD-PICRUSt Compatibility Project

Introduction:
PICRUSt is a bioinformatics package developed by Dr. Morgan Langille and his team that allows one to predict the functionality of bacterial samples based on phylogeny. It is designed to estimate gene families contributed to a metagenome by bacteria or archaea using 16S rRNA sequencing. The goal is to predict the functionality of a bacterial sample by inferring the traits of living organisms that haven’t been studied in depth.
The goal for the HOMD-PICRUSt Compatibility project is to extract bacterial data from the HOMD Database in order to recreate a species tree, a 16S gene count table, and an enzyme count table for use with PICRUSt.

Python Scripts:

  homd_read.py:
    This script requires the sorted text versions of the HOMD KEGG bacterial data. For each unique orf value where the value 
    of dr = EC, the corresponding dr_id values were appended to a list. Each unique orf is then printed with its most common 
    dr_id. If multiple modes were found for an orf, a Counter was object then used in order to get the most common dr_id. 
    Selecting the most common dr_id in this fashion can lead to changes in the .parsed files that are outputted due to the 
    randomization seen when dr_ids with the same mode are listed. 
    For example: Values x,y,z have the same mode --> (x,y,z) or (x,z,y) or (y,x,z) or (y,z,x) or (z,x,y) or (z,y,x)
    Uses Python 3.5.1
  
  enzyme_count.py:
    This script requires the use of "names.txt" in order to open the proper .parsed files. The file "enzyme_columns.txt" 
    contains numerical values that correspond to all the enzymes that are seen in the .parsed files. The script counts the 
    number of times each of the enzymes from "enzyme_columns.txt" appears in a specific .parsed file. The script will then 
    output the respective .count files. Uses Python 2.7.12
    
  homd_16s_count_generator.py:
    This script requires the 16S Newick Table found on the HOMD website. The script appends each sequence ID into a list, and 
    a counter object is then used to find the counts of each sequence ID. The output is a tab-delimited table that contains
    the sequence ID followed by its 16s gene count. Uses Python 2.7.12
    
  homd_main_table.py:
    This script requires the use of "names.txt" in order to access the short abbreviated names of the bacterial files.
    The file "NameMap2.txt" is then used in order to replace the abbreviated names with the respective sequence IDs. To get 
    all the numerical enzyme values into a list, "enzyme_columns.txt" was then opened. Then, the .count files were opened and
    the enzyme count values were all appended to an initial list before that list was then appended to another list. The 
    numerical enzyme values were then printed in tab-delimited format (columns) and the sequence ID along with their 
    respective enzyme counts were printed (rows). Uses Python 2.7.12
