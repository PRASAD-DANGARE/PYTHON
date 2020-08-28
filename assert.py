# Python Program To Handle The Assertion Exception That Is Given By Assert Statement

'''
Function Name    :  Assertion Exception Handling
Function Date    :  27 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''


x = int(input('Enter A Number Greater Than 0 : '))
try:
    assert(x>0) # Exception May Occure
    print('This Number Is Greater Than 0 :', x)
except AssertionError:
    print("Wrong Input Entered") # This Is Executed In Case Of Exception.
    
    