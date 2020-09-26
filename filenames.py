# Python Program To Display All Contents Of The Current Directory

'''
Function Name    :  Display All Contents Of The Current Directory
Function Date    :  26 Sep 2020
Function Author  :  Prasad Dangare
'''

import os
for dirpath, dirnames, filenames in os.walk('.'):
    print('Current Path : ', dirpath)
    print('Directories : ', dirnames)
    print('Files : ', filenames)
    print()
    