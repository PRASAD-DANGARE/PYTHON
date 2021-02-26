'''
Description      :  Demonstration Of Recursion And It's Scope
Function Date    :  26 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

print("Demonstration of Scope of Recursion")

import sys

print("Maximum number of recursive call are {} in python".format(sys.getrecursionlimit()))

sys.setrecursionlimit(1500) # Changing recursion limit

print("Maximum number of recursive call are {} in python".format(sys.getrecursionlimit()))

def fun(): # Recursive function which goes into infinite recursive calls
    print("Inside fun")
    fun()

i = 1

def gun(): # Recursive function which performs recursive calls 10 times

    global i
    if(i <= 10):
        print(i)
        i += 1
        gun()
gun()

def fact(no):
    if(no == 0):
        return 1
    return no * fact(no - 1)
    
value = 5
ret = fact(value)
print("Factorial of {} is {}".format(value, ret))