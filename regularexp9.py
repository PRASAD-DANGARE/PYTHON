# Python Program To Create A Regular Expression To Retrieve All Words Having 5 Characters Length Using Search()

'''
Function Name    :  Regular Expression Using search()
Function Date    :  27 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import re
str = 'One Two Three Four Five Six Seven 8 9 10'
result = re.search(r'\b\w{5}\b', str)

# To Retrieve The Word From Result Object, Use group()

print(result.group())

