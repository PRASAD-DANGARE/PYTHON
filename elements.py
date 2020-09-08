# Python Program A Function To Display A Group Of String 

'''
Function Name    :  Function To Display A Group Of String. 
Function Date    :  8 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String  
'''

def display(lst):
    """ To Display The String """
    
    for i in lst:
        print(i)
        
# Take A Group Of String From Keyboard

print('Enter String Seprated By Comma : ')
lst = [x for x in input().split(',')]

# Call Display() And Pass The List

display(lst)