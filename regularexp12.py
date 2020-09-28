# Python Program To Create A Regular Expression To Retrieve Only Single Digits From String

'''
Function Name    :  Regular Expression To Retrieve Single Digits From String
Function Date    :  28 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''


import re
str = 'one two three four five six seven 8 9 10'
result = re.findall(r'\b\d\b', str)
print(result)

