'''
Description      :  Use Of Local Scope
Function Date    :  05 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''


x = 50

def func(x):
    print ('x is', x)
    x = 2
    print ('Changed local x to', x)

func(x)
print ('x is still', x)