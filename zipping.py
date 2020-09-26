# Python Program To Compress The Contents Of Files

'''
Function Name    :  Zipping The Contents Of Files
Function Date    :  26 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

from zipfile import*

f = ZipFile('test.zip', 'w', ZIP_DEFLATED) # Create Zip File

# Add Some Files. These Are Zipped

f.write('file1.txt')
f.write('file2.txt')
f.write('file3.txt')

# Close The Zip File

print('test.zip File Created...')
f.close()

