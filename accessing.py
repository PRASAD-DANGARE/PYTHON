# Python Program To Access The Characters Of A String Using For-Loop

'''
Function Name    :  Access Characters Of String . 
Function Date    :  1 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

str = 'Core Python'

# Access Each Letter Using For-Loop

for i in str:
    print(i, end= ' ')
    
print() # Put Cursor Into Next Line

# Access In Reverse Order

for i in str[:: -1]:
    print(i, end= " ")
    