# Python Program To Retrieve Data From A File Using Regular Expression And Then Write That Data Into File

'''
Function Name    :  Regular Expression That Retrieve Data From A File
Function Date    :  29 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import re

f1 = open('salaries.txt', 'r') # Open The Files
f2 = open('newfile.txt', 'w')

for line in f1: # Repeat For Each Line Of The File f1
    res1 = re.search(r'\d{4}', line) # Extract id No From f1
    res2 = re.search(r'\d{4,}.\d{2}', line) # Extract Salary From f1
    f2.write(res1.group()+"\t") # Write id No Into f2
    f2.write(res2.group()+"\n") # Write Salary Into f2
    
# Close The Files

f1.close()
f2.close()

