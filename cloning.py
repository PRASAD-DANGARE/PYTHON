# Python Program To Understand The Use Of Cloning In List


'''
Function Name    :  Cloning In List.
Function Date    :  10 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

x = [10,20,30,40,50]
y = x[:] # x Is Cloned As y
print(x)
print(y)

x[1] = 99 # Modify 1st Element In x
print(x)
print(y)