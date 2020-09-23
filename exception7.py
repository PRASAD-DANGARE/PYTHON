# Python Program Using The Assert Statement And Catching AssertionError


'''
Function Name    :  Usage Assert Statement And Catching AssertionError
Function Date    :  23 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

try:
    x = int(input('Enter A Number Between 5 And 10 : '))
    assert x > 5 and x <= 10, "Your Input Is not Correct"
    print('The Number Entered : ', x)
    
except AssertionError as obj:
    print(obj)
    