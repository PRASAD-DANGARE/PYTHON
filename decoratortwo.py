# Python Program To Create Two Decorator


'''
Function Name    :  Create Two Decorator. 
Function Date    :  9 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

def decor(fun):
    def inner():
        value = fun()
        return value+2
    return inner

# A Decorator That Double The Value Of A Function

def decor1(fun):
    def inner():
        value = fun()
        return value * 2
    return inner 

# Take A Funtion To Which Decorator Should Be Applied

def num():
    return 10

# Call num() Function And Appky Decor1 And Then Decor

result_fun = decor(decor1(num))
print(result_fun())