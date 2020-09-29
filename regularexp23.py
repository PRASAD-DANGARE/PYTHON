# Python Program To Create A Regular Expression That Reads Email-ids From A Text File

'''
Function Name    :  Regular Expression That Reads Email-ids From A Text File
Function Date    :  29 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''


import re

f = open('mails.txt', 'r') # Open The File For Reading

for line in f: # Repeat For Each Line Of The File
    res = re.findall(r'\S+@\S+', line)
    
if len(res)>0: # Display If There Are Some Elements In Result 
    print(res)
    
# Close The File

f.close()



