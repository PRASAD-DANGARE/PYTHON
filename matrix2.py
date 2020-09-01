# Python Program To Accept Two Matrices And Find Their Product
# Matrix Multiplication

'''
Function Name    :  Accepts Two Matrix And Find Their Product. 
Function Date    :  1 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

import sys
from numpy import*

# Accept Numbers Of Rows And Cols Of First Matrix Into r1, c1

r1, c1 = [int(a) for a in input("First Matrix rows, columns : ").split()]
print("\n")

#  Accept Numbers Of Rows And Cols Of First Matrix Into r2, c2

r2, c2 = [int(a) for a in input("Second Matrix Rows, Columns : ").split()]
print("\n")

# Test The Conditions If c1 != r2 Then Multiplication Is Not Possible

if c1 != r2:
    print('Multiplication Is Not Possible')
    sys.exit() # Terminate The Program
    
# Accept First Matrix Elements As A String Into str1

str1 = input('Enter First Matrix Elements :\n ')
print("\n")

# Convert str1 Into A Matrix With Size r1xc1

x = reshape(matrix(str1), (r1, c1))

# Accepts Second Matrix Elements As A String Into str2

str2 = input('Enter Second Matrix Elements:\n ')
print("\n")

# Convert str2 Into A Matrix With Size r2xc2

y = reshape(matrix(str2), (r2, c2))
print('The Product Matrix : ')
print("\n")
z = x * y
print(z)