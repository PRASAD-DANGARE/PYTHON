# Python Program To Overload Greater > Operator To Make It Act On Class Objects

'''
Function Name    :  Overload Greater Operator On Class Objects 
Function Date    :  20 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

class Ramayan:
    def __init__(self, pages):
        self.pages = pages
        
    def __gt__(self, other):
        return self.pages>other.pages
    
class Mahabharat:
    def __init__(self, pages):
        self.pages = pages
        
b1 = Ramayan(1000)
b2 = Mahabharat(1500)
if (b1 > b2):
    print('Ramayan Has More Pages')
else:
    print('Maharabhat Has More Pages')
    
    