# Python Program To Accept A Matrix From The Keyboard And Display Its Transpose Matrix

'''
Function Name    :  Accepts A Matrix And Display Its Transpose Matrix. 
Function Date    :  1 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

from numpy import*

# Accept Matrix Of Rows And Column Into r, c

r, c = [int(a) for a in input("Enter Rows, Columns : ").split()]
print("\n")

# Accept Matrix Elements As A String Into str

str = input('Enter Matrix Elements :\n ')
print("\n")

# Convert The String Into A Matrix With Size rxc

x = reshape(matrix(str), (r, c))
print('The Original Matrix : ')
print("\n")
print(x)
print("\n")

print('The Transpose Matrix : ')
y = x.transpose()
print("\n")
print(y)
print("\n")