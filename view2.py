# Python Program To Copy An Array As Another Array Using copy() Method

'''
Function Name    :  Create A Copy Of Array As Another Array Using copy() Method. 
Function Date    :  31 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

from numpy import*

a = arange (1, 6) # It Create Elements From 1 To 5
b = a.copy() # Create a Copy Of a And Call It b

print(' Original Array : ', a)
print('Newly Array : ', b)
print("\n")


b[0] = 99 # Modify oth Element Of b With The Value 99

print('After Modification Replace 0th Value With 99 : ')
print("\n")

print('Original Array : ', a)
print('Newly Array : ', b)
print("\n")
