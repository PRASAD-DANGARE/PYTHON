# python program to know the effect of any() and all() function

'''
Function Name    :  Use Of Any And All Functions. 
Function Date    :  28 Aug 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

from numpy import*

a = array([1, 2, 3, 0])
b = array([0, 2, 3, 1])

c = a > b
print('\n Result Of a > b : ', c)
print("\n")


print('Check If Any One Elements Is True : ', any(c))
print("\n")

print('Check If All Elements Are True : ', all(c))
print("\n")

if(any(a > b)):
    print('a Contains Atleast One Elements Greater Than Those Of b')
    print("\n")