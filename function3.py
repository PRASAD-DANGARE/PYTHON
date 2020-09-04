# Python Program To Test Wether A Number Is Even Or Odd

'''
Function Name    :  Test Wether A Number Is Even Or Odd. 
Function Date    :  4 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer,String
'''

def even_odd(num):
    """To Know num Is Even Or Odd"""
    if num % 2 == 0:
        print(num, "Is Even")
        
    else:
        
        print(num, "Is Odd")
        
# Call The Function

even_odd(12)
even_odd(13)
