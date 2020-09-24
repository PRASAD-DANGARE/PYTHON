# python program to know whether a file exists or not

'''
Function Name    :  know whether a file exists or not
Function Date    :  24 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import os, sys

# open the file for reading data

fname = input('Enter Filename : ')

if os.path.isfile(fname):
    f = open(fname, 'r')
else:
    print(fname+'does not exist')
    sys.exit()
    
# read strings from the files

print('the file contents are : ')
print(str)

# closing the file

f.close()
