# Python Program To Access Global Variables Inside A Function And Modify It

'''
Function Name    :  Access Global Variable Inside Function And Modify It. 
Function Date    :  7 Sep 2020
Function Author  :  Prasad Dangare
'''

a = 1 # Global Variable
def myfunction():
    global a # This Is Global Variable
    print('Global a = ', a) # Display Global Variable
    a = 2 # Modify Global Variable Value
    print('Modified a = ', a) # Display Modified Value
    
myfunction()
print('Global a = ', a) # Display Modified Value