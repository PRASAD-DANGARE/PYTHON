# python program to create an array with 5 equal points using linespace() method

'''
Function Name    :  Create Array With 5 Equal Points Using linespace(). 
Function Date    :  28 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Float
'''

from numpy import*
from numpy.core.function_base import linspace

# divide 0 to 10 into 5 parts and take those points in the array

a = linspace(0, 10, 5)
print('a = ', a)
