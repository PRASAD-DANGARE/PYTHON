# Python Program To Display All Positions Of A Sub String In A Given Main String 

'''
Function Name    :  Display All Position Of A Sub String In Main String . 
Function Date    :  2 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  Integer 
'''

str = input('Enter Main String : ')
print("\n")

sub = input('Enter Sub String : ')
print("\n")

i = 0
flag = False # Becomes True If String Is Found
n = len(str)
while i < n: # Repeat From 0th To nth Characters
    pos = str.find(sub, i, n) 
    if pos != -1: # If Found Display Its Position
        print('Found At Position : ', pos + 1)
        print("\n")
        i = pos + 1 # Search From pos+1 Position Onwards
        flag = True
    else:
        i = i + 1 # Search From Next Characters Onwards
    if flag == False:
        print('Sub String Not Found')
        print("\n")