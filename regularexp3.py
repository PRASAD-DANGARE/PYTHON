# Python Program To Create A Regular Expression Using The match() Method 
# To Search For String Starting With m And Having Total 3 Characters

'''
Function Name    :  Regular Expression To Search String Using match()
Function Date    :  27 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import re
str = 'Man Sun Mop Run'
result = re.match(r'm\w\w', str)
print(result.group())
