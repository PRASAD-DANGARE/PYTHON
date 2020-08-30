# Python Program To Alias An Array And Understand The Affect Of Aliasing

'''
Function Name    :  Alias An Array To See The Affect Of Aliasing. 
Function Date    :  30 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

from numpy import*

a = arange(1, 6) # Create a With Elements 1 To 5
b = a # Give Another Name To b To a

print('\n Original Array : ', a)
print('Alias Array : ', b)
print("\n")

b[0] = 99 # Modify oth Elements Of b
print('After Modification : ')
print("\n")

print('Original Array : ', a)
print('Alias Array: ', b)
print("\n") 