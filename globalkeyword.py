# Python Program To Understand Global And Local Variables

'''
Function Name    :  Use Of Global Variable And Local Variable. 
Function Date    :  7 Sep 2020
Function Author  :  Prasad Dangare
'''

a = 1 # This Is Global Variable
def global_localfunction():
    a = 2 # This Is Local Variable
    print('a = ', a) # Display Local Variable
global_localfunction()
print(' a = ', a) # Display Global Variable



