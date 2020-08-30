# Python Program To Compare The Corresponding Elements Of Two Array And Retrive The Biggest Elements.

'''
Function Name    :  Compare The Corresponding Elements Of Two Array. 
Function Date    :  28 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

from numpy import*

a = array([10, 20, 30, 40, 50], int)
b = array([1, 21, 3, 40, 51], int)

c = where(a > b, a, b)

print(c)
