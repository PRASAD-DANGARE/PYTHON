# Python Program To Apply A Decorator To A Function Using @ Symbol

'''
Function Name    :  Apply A Decorator To A Function Using @. 
Function Date    :  9 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

def decor(fun): # This Is Decorator Function
    def inner(): # This Is The Inner Function That Modifies
        value = fun()
        return value+2
    return inner # Return inner function
    
# Take A Function To Which Decorator Should Be Applied

@ decor # Apply decor To The Below Function
def num():
    return 10

# Call num() Function And Display Its Result

print(num())
  