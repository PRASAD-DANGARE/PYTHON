# Creating Array From Another Array Using numpy 

'''
Function Name    :  Create Array From Another Array Using numpy. 
Function Date    :  28 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

from array import array
from numpy import *

a = array ([ 1, 2, 3, 4, 5])
b = array (a) # Create b From a Using Array() Function
c = a # Create c Assignment a To c 

# Display The Arrays

print("a = ", a)
print("b = ", b)
print("c = ", c)
