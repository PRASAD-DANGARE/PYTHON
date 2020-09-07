# Python Program To Pass An Integer To A Function And Modify It

'''
Function Name    :  Pass An Integer To A Function And Modify It. 
Function Date    :  6 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

def modify(x):
    """ Reassign A Value To The Variable """
    
    x = 15
    print(x, id(x))
    
# Call Modify() And Pass x

x = 10
modify(x)
print(x, id(x))