# Python Program To Calculate Factorial Value Of Numbers

'''
Function Name    :  Calculate Factorial Of Numbers. 
Function Date    :  4 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer,String
'''

def fact(n):
    """To Find Factorial Value"""
    
    prod=1
    while n>=1:
        prod*=n
        n-=1
        
    return prod

# Display Factorial Of First 10 Numbers
# Call Fact() Function And Pass The Number From 1 To 10

for i in range(1, 11):
    print('\n Factorial Of {} Is {}'.format(i, fact(i)))
    
