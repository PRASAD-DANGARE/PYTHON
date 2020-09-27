# Python Program To Create A Regular Expression To Retrieve All The Words 
# That Are Having The Length Of At Least 4 Characters

'''
Function Name    :  Regular Expression To Retrieve 4 Characters
Function Date    :  27 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import re
str = 'One Two Three Four Five Six Seven 8 9 10'
result = re.findall(r'\b\w{4,}\b', str)
print(result)

