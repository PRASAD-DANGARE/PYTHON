'''
Description      :  Use Of DocString In Function 
Function Date    :  05 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''


def print_max(x, y):

    '''    Prints The Maximum Of Two Numbers.
    The Two Values Must Be Integers.'''
 
    # convert to integers, if possible
    
    x = int(x)
    y = int(y)

    if x > y:
        print (x, 'is maximum')
    else:
        print (y, 'is maximum')

print_max(3, 5)
print (print_max.__doc__)
