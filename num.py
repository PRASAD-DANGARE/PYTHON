# Python Program To Perform Mathematical Operations On numpy Array

'''
Function Name    :  Mathematical Operations On Numpy Array. 
Function Date    :  29 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Float
'''

from numpy import*

arr = array([10, 20, 30.5, -40])
print("Original Array : ", arr)
print("\n")

print("After Add 5 : ", arr + 5)
print("Next \n")

print("After Subtract 5 : ", arr - 5)
print("Next \n")

print("After Multiply 5 : ", arr * 5)
print("Next \n")

print("After Division 5 : ", arr / 5)
print("Next \n")

print("After Moduls 5 : ", arr % 5)
print("Next \n")

print("Expression Value : ", (arr + 5)** 2 - 10)
print("Next \n")

print("Sin Value : ", sin(arr))
print("Next \n")

print("Cos Value : ", cos(arr))
print("Next \n")

print("Tan Value : ", tan(arr))
print("Next \n")

print("Big Elements : ", max(arr))
print("Next \n")

print("Small Elements : ", min(arr))
print("Next \n")

print("Sum Of Elements : ", sum(arr))
print("Next \n")

print("Average Value : ", mean(arr))
print("Last \n")