# Python Program To Create A Regular Expression To Search At The Ending Of A String By Ignoring The Case

'''
Function Name    :  Regular Expression To Search String Using re.IGNORECASE
Function Date    :  29 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import re
str = "Hello World"
res = re.search(r"World$", str, re.IGNORECASE)
if res:
    print("String Ends With 'World' ")
else:
    print("String Does Not End With 'World' ")
    