# Python Program To Create An Array Using logspace()

'''
Function Name    :  Create Array Using logspace(). 
Function Date    :  28 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Float
'''

from numpy import*
from numpy.core.function_base import logspace

# Divide The Range: 10 Power 1 To 10 Power Into 5 Equal Parts
# And Take Those Points In The Array

a = logspace(1, 4, 5)

# Find Number Of Elements In a

n = len(a)

# Repeat From 0 To n-1 In a

for i in range(n):
    print("%1f" % a[i], end= ' ') # Display 1 Digit After Decimal Points