# Python Program To Create A Regular Expression To Retrieve All Words Starting With P In A Given String

'''
Function Name    :   Regular Expression To Retrieve All Words Starting With P
Function Date    :  27 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import re
str = 'One Programmer Replace By Another Programmer '
result = re.findall(r'P[\D]*', str)

# findall() Returns A List , Retrieve The Elements From List

for word in result:
    print(word)
    