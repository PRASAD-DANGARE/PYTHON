# Python Program To Create A Regular Expression To Retrieve The Timings Either 'am' Or 'pm'

'''
Function Name    :  Regular Expression To Retrieve Timings 'am' Or 'pm'
Function Date    :  29 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''


import re
str ='The Meeting May Be At 8am Or 9am Or 4pm Or 5pm'
res = re.findall(r'\dam|\dpm', str)
print(res)

