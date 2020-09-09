# Python Program To Apply Two Decorator To The Same Function Using @ Symbol

'''
Function Name    :  Apply 2 Decorator To Same Function Using @. 
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

# Take A Function To Which Decorator Should Be Applied

@ decor
@ decor1
def num():
    return 10

# Call num() Function And Apply Decor1 And Then Decor

print(num())