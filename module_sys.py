'''
Description      :  Use Of Module sys 
Function Date    :  06 Feb 2021
Function Author  :  Prasad Dangare
Input            :  str
Output           :  str

'''

import sys

print('The command line arguments are:')

for i in sys.argv:
    print (i)

print ('\n The Python Path Is : ', sys.path, '\n')