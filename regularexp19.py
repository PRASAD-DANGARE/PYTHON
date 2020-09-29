# Python Program To Create A Regular Expression To Search For A Word At The Ending Of A String

'''
Function Name    :  Regular Expression To Search Word At Ending Of String
Function Date    :  29 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import re
str = "Hello World"
res = re.search(r"World$", str)
if res:
    print("String Ends With 'World' ")
else:
    print("String Does Not End With 'World' ")
    