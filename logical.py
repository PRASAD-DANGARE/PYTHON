# Python Program To Understand The Use Of Logical Functions On Array

'''
Function Name    :  Logical Functions On Array Using and, or, not. 
Function Date    :  28 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Float
'''

from numpy import*

a = array([1, 2, 3], int)
b = array([0, 2, 3], int)

c = logical_and(a > 0 , a < 4)
print(c)

c = logical_or(b >= 0 , b == 1)
print(c)

c = logical_not(b)
print(c)
