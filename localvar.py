# Python Program To Understand The Use Of Local Variable
# Local Variable In A Function

'''
Function Name    :  Understand The Use Of Local Variable. 
Function Date    :  7 Sep 2020
Function Author  :  Prasad Dangare
'''

def localfunction():
    p = 1 # This Is Local Variable
    p += 1 # Increment It
    print(p)
    
localfunction()
print(a) # error a Is Removed From The Memory It Is Not In Local Variable Of A Function, a Is Not Defined