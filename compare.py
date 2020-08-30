# Python Program To Compare Two Array And Display The Resultant Boolean Type Array

'''
Function Name    :  Compare Two Arrays. 
Function Date    :  28 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Charactor
Output           :  Charactor
'''

from numpy import*

a = array([1, 2, 3, 0])
b = array([0, 2, 3, 1])

c = a == b
print('Result Of a == b : ', c)

c = a > b
print('Result Of a == b : ', c)

c = a <= b 
print('Result Of a == b : ', c)
