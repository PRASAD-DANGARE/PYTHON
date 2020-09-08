# Python Program To Calculate Factorial Values Using Recursion

'''
Function Name    :  Calculate Function Values Using Recursion. 
Function Date    :  8 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer  
'''

def factorial(n):
    """ To Find Factorial Of n """
    
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    return result

# Find Factorial Values For First 10 Numbers

for i in range(1, 11):
    print('Factorial Of {} Is {} '.format(i, factorial(i)))
    