# Python Program To Get  Copy Of Global Variables Into A Function And Work With It
# Same Name For Global And Local Variables

'''
Function Name    :  Use Of globals() In A Function. 
Function Date    :  7 Sep 2020
Function Author  :  Prasad Dangare
'''

a = 1 # Global Variable
def global_localfunction():
    a = 2 # a Is Local Variable
    x = globals()['a'] # Get Global Variable Into x
    print('Global Var a = ', x)
    print('Local Var a = ', a)
    
global_localfunction()
print('Global Var a = ', a)

    