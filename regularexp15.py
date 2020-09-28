# Python Program To Create A Regular Expression To Extract Only Name But Not Number From String

'''
Function Name    :  Regular Expression To Extract Only Name Not Number
Function Date    :  28 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  Integer
'''

import re
str = 'Prasad Dangare : 7057113124'
res = re.search(r'\D+', str)
print(res.group())

