# Python Program To Create A Regular Expression To Replace A String With A New String

'''
Function Name    :  Regular Expression To Replace A String With A New String
Function Date    :  27 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import re
str = 'Logic Building Is Starting From Next Week At 8.00 pm'
res = re.sub(r'Week', 'Tuesday', str)
print(res)
