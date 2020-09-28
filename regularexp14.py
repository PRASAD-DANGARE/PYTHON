# Python Program To Create A Regular Expression To Retrieve The Phone Number Of A Person

'''
Function Name    :  Regular Expression To Retrieve Phone Number Of A Person
Function Date    :  28 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  Integer
'''

import re
str = 'Prasad Dangare : 7057113124'
res  = re.search(r'\d+', str)
print(res.group())

