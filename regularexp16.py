# Python Program To Create A Regular Expression To Find All Words Starting With 'an' Or 'ak'

'''
Function Name    :  Regular Expression To Find Words Start With an,ak
Function Date    :  28 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import re
str = 'Anil Akhil Anant Arun Aarti Arundhati Abhijit Ankur'
res = re.findall(r'A[nk][\w]*', str)
print(res)

