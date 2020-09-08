# Python Program To Understand The Use Of Global Variable 

'''
Function Name    :  Understand The Use Of Global Variable. 
Function Date    :  7 Sep 2020
Function Author  :  Prasad Dangare
'''

a = 1 # Global Variable
def globalfunction():
    b = 2 # Local Variable
    print('a = ', a) # Display Global Variable
    print('b = ', b) # Display Local Variable
    
globalfunction()
print(a) # Available
print(b) # error Not Available
 