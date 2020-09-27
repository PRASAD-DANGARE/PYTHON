# Python Program To Create A Regular Expression To Retrieve All  Words Having 5 Characters Length

'''
Function Name    :  Regular Expression To Retrieve 5 Letter Words
Function Date    :  27 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import re
str = 'One Two Three Four Five Six Seven 8 9 10'
result = re.findall(r'\b\w{5}\b', str)
print(result)

