'''
Description      :  Use Of Keyword Arguments In Function 
Function Date    :  05 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''

def func(a, b = 5, c = 10):
     
    print ('A Is', a, 'And B Is', b, 'And C Is', c)

func(3, 7, 11) # First Is Taken A
func(25, c = 24)
func(c = 50, a = 100)