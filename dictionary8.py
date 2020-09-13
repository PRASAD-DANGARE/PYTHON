# Python Program To Create A Dictionary That Does Not Change The Order Of Elements

'''
Function Name    :  Create Dictionary That Does Not Change The Order Of Elements.
Function Date    :  13 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

from collections import OrderedDict
d = OrderedDict() # d Is Ordered Dictionary
d[10] = 'A'
d[11] = 'B'
d[12] = 'C'
d[13] = 'D'

# Display The Ordered Dictionary

for i, j in d.items():
    print(i, j)
    