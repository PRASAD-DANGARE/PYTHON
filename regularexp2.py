# Python Program To Create A Regular Expression To Search For String Starting With m
# And Having Total 3 Characters Using findall() Method

'''
Function Name    :  Regular Expression To Search String Using findall()
Function Date    :  27 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import re
str = 'Man Sun Mop Run'
result = re.findall(r'm\w\w', str)
print(result)
