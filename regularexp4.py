# Python Program To Create A Regular Expression To Split A String Into Pieces 
# Where One Or More Non Alpha Numeric Characters Are Found

'''
Function Name    :  Regular Expression To Search String Using split()
Function Date    :  27 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import re
str = 'We; Are Learning: "Core" Python\s'
result = re.split(r'\W+', str)
print(result)

