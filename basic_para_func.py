'''
Description      :  Use Of Function Parameters
Function Date    :  05 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''


def print_max(a, b):
     
    if a > b:
        print (a, 'is maximum')
    
    elif a == b:
        print (a, 'is equal to', b)
    else:
        print (b, 'is maximum')
    
    # directly pass literal values

print_max(1, 2)
x = 5
y = 5

# pass variables as arguments

print_max(x, y)