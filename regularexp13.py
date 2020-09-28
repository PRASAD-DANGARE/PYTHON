# Python Program To Create A Regular Expression To Retrieve The Last Word Of A String, If The Starts With t

'''
Function Name    :  Retrieve Last Word Of A String Starts With t
Function Date    :  28 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import re
str = 'one two three one two three'
result = re.findall(r't[\w]*\Z', str)
print(result)

