# Python Program To Increase The Value Of A Function By 2

'''
Function Name    :  Increase The Value Of A Function By 2. 
Function Date    :  9 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

def decor(fun): # This Is Decorator Function
    def inner(): # This Is The Inner Function That Modifies
        value = fun()
        return value+2
    return inner # Returns Inner Function

# Take A Function To Which Decorator Should Be Applied

def num():
    return 10

# Call Decorator Function And Pass num

result_fun = decor(num) # result_fun Represent Inner Function 
print(result_fun()) # Call result_fun And Display The Result
    