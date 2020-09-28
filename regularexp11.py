# Python Program To Create A Regular Expression To Retrieve All Words With 3 Or 4 Or 5 Characters Length

'''
Function Name    :  Regular Expression To Retrieve 3,4,5 Characters
Function Date    :  28 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import re
str = 'one two three four five six seven 8 9 10'
result = re.findall(r'\b\w{3,5}\b', str)
print(result)


 