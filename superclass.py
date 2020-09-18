# Python Program To Call The Super Class Constructor In The Sub Class Using super()

'''
Function Name    :  Super Class Constructor In The Sub Class Using super()
Function Date    :  18 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

class Father:
    def __init__(self, property = 0):
        self.property = property
        
    def display_property(self):
        print('Father\' S property = ', self.property)
        
class Son(Father):
    def __init__(self, property1 = 0, property = 0):
        super().__init__(property)
        self.property1 = property1
        
    def display_property(self):
        print('Total Property Of Child = ', self.property1 + self.property)
        
# Create Sub Class Instance And Display Father's Property

s = Son(2000000.00, 80000000.00)
s.display_property()
    