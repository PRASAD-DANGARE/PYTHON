# Python Program To Create A Regular Expression To Retrive All Words Starting With A Numerical Digit

'''
Function Name    :  Regular Expression To Retrieve All Numeric Digit
Function Date    :  27 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import re
str = 'The Meeting Will Be Conducted On 9th And 10th Of Every Month'
result = re.findall(r'\d[\w]*', str)
for word in result:
    print(word)
    