# Python Program To Unzip The Contents Of The Files That Are Available In A Zip File

'''
Function Name    :  Unzip The Contents Of The Files
Function Date    :  26 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

from zipfile import*

z = ZipFile('test.zip', 'r') # Open The Zip File

z.extractall() # Extract All File Names Which Are In The Zip File
