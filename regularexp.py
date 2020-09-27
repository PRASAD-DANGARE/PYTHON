# Python Program To Create A Regular Expression To Search For String Starting With m 
# And Having Total 3 Characters Using The Search() Method.

'''
Function Name    :  Regular Expression To Search String Using search()
Function Date    :  27 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''


import re

str = 'Man Sun Mop Run'
result = re.search(r'm\w\w', str)
if result: # If Result Is Not None 
    print(result.group())
