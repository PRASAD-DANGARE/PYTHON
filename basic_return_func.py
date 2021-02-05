'''
Description      :  Use Of Return Statement In Function 
Function Date    :  05 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''

def maximum(x, y):
 
 if x > y:
    return x 
 
 elif x == y:
    return 'The Numbers Are Equal'
 
 else:
    return y

print (maximum(2, 3))
print (maximum(3, 3))
print (maximum(-1, 0))
