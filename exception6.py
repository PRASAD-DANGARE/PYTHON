# Python Program To Understand The Usage Of try With finally Blocks


'''
Function Name    :  Usage Of try With finally Blocks
Function Date    :  23 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

try:
    x = int(input('Enter A Number : '))
    y = 1 / x
    
finally:
    print("We Are Not Catching The Exception.")
print("The Inverse Is : ", y)
