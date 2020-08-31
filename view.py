# Python Program To Create A View Of An Existing Array

'''
Function Name    :  Create A View Of An Existing Array. 
Function Date    :  31 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

from numpy import*

a = arange (1, 6) # It Create Elements From 1 To 5
b = a.view() # Create a View Of a And Call It b

print('\n Original Array : ', a)
print('Newly Array : ', b)
print("\n")


b[0] = 99 # Modify oth Element Of b With The Value 99

print('After Modification Replace 0th Value With 99 : ')
print("\n")

print('Original Array : ', a)
print('Newly Array : ', b)
print("\n")
