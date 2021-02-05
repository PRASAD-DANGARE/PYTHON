'''
Description      :  Use Of Global Scope
Function Date    :  05 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''

x = 50

def func():

    global x
    print ('x is', x)
    
    x = 2
    print ('Changed global x to', x)

func()
print ('Value of x is', x)
