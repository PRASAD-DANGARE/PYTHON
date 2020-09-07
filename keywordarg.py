# Python Program To Understand The Keyword Argument Of A Function

'''
Function Name    :  Use Keyword Argument In A Function . 
Function Date    :  6 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String  
'''

def grocery(item, price):
    """ To Display The Given Arguments """
    
    print('\n Item kg = %s' % price)
    print('Price = %.2f' % item)
    print("\n")
    
# Call Grocery() And Pass 2 Arguments

grocery(price = 'Sugar', item = 50.75) # Keyword Arguments
grocery(item = 20.00, price = 'Salt') # Keyword Arguments