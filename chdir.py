# Python Program To Change To Another Directory

'''
Function Name    :  Change To Another Directory
Function Date    :  26 Sep 2020
Function Author  :  Prasad Dangare
'''

import os

goto = os.chdir('newsub/newsub2') # Change To newsub2 Directory

current = os.getcwd() # Get Current Working Directory
print('Current Directory = ', current)



