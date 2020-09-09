# python program a lambda function to calculate product of elements of a list

'''
Function Name    :  Calculate Product Of Elements Of List. 
Function Date    :  9 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

from functools import*
lst = [1,2,3,4,5]
result = reduce(lambda x, y: x*y, lst)
print(result)
