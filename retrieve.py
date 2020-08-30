# Python Program To Retrive Non Zero-Elements From An Array

'''
Function Name    :  Retrive Non Zero-Elements . 
Function Date    :  29 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

from numpy import*

a = array([1, 2, 0, -1, 0, 6],  int)
c = nonzero(a)

for i in c:
    print(i)
    print(a[c])
    