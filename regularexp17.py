# Python Program To Create A Regular Expression To Retrieve Data Of Births From String

'''
Function Name    :  Regular Expression To Retrieve Data Of Births From String
Function Date    :  28 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  Integer
'''

import re
str = 'vijay 20 1-5 2001, rohit 21 22-10-1990, sita 22 15-09-2000'
res = re.findall(r'\d{2}-\d{2}-\d{4}', str)
print(res)

