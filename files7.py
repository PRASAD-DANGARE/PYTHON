# Python Program To Count Numbers Of Lines, Words And Characters In A Text File

'''
Function Name    :  Count Numbers Of Lines, Words, Characters In Text File
Function Date    :  24 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import os, sys

# Open The File For Reading Data

fname = input('Enter Filename : ')

if os.path.isfile(fname):
    f = open(fname, 'r')
else:
    print(fname+'Does Not Exist')
    sys.exit()
    
# Initialize The Counters To 0

cl = cw = cc = 0

# Read Line By Line From The Files

for line in f:
    words = line.split()
    cl += 1
    cw += len(words)
    cc += len(line)
    
print('no. of lines : ', cl)
print('no. of words : ', cw)
print('no. of characters : ', cc)

# Close The File

f.close()

