# Python Program To Create A Regular Expression To Search Whether A Given String Is Starting With 'He' Or Not

'''
Function Name    :  Regular Expression To Search String Is Starting With 'He'
Function Date    :  29 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import re
str = 'Helo Guys'
res = re.search(r"^He", str)
if res:
    print("String Starts With 'He' ")
else:
    print("String Does Not Starts With 'He' ")
    