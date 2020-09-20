# Python Program To Use Addition Operator To Add The Contents Of Two Objects

'''
Function Name    :  Use Addition Operator To Add Contents Of 2 Object
Function Date    :  20 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

class BookX:
    def __init__(self, pages):
        self.pages = pages
        
    def __add__(self, other):
        return self.pages+other.pages
    
        
class BookY:
    def __init__(self, pages):
        self.pages = pages
        
b1 = BookX(100)
b2 = BookY(150)
print('Total pages = ', b1+b2) 

