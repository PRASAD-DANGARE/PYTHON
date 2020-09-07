# Python Program To Understand The Use Of Default Arguments In A Function

'''
Function Name    :  Use Default Argument In A Function. 
Function Date    :  6 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String  
'''

def grocery(item, price = 40.00):
    """ To Display The Given Arguments """
    
    print('Item = %s' % item)
    print('Price = %2.f' % price)
    
# Call Grocery() And Pass Arguments

grocery(item = 'Sugar', price = 50.75) # Pass 2 Arguments
grocery(item = 'Salt') # Default Value For Price Is Used