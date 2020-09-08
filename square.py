# Python Program To Find Square Of Elements In A List

'''
Function Name    :  Square Of Elements In A List. 
Function Date    :  8 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

def square(x):
    return x*x

# Let Us Take A List Of Numbers

lst = [1,2,3,4,5]

# Call map() With Square() And lst

lst1 = list(map(square, lst))
print(lst1)