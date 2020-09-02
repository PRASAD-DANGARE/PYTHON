# Python Program To Display All Positions Of A Sub String In A Given Main String
# To Find All Occurrence Of Sub String In A Main String Using pos -1

'''
Function Name    :  All Occurance Of Sub String In A Main String . 
Function Date    :  2 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  Integer 
'''

str = input('Enter Main Strings : ')
print("\n")

sub = input('Enter Sub Strings : ')
print("\n")

flag = False
pos = -1
n = len(str)
while True: # repeat forever
    pos = str.find(sub, pos + 1, n)
    if pos == -1: 
        break
    
    print('Found At Position : ', pos + 1)
    print("\n")
    flag = True
    
if flag == False:
    print('Not Found')
    print("\n")