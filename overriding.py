# Python Program To Override Super Class Constructor And Method In Sub Class

'''
Function Name    :  Overriding Base Class Constructor And Method In Sub Class
Function Date    :  18 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

class Father:
    def __init__(self):
        print('Father\'S property = ', self.property)
        
class Son(Father):
    
    def __init__(self):
        self.property = 2000000.00
        
    def display_property(self):
        print('Child\ S property = ', self.property)
        
# Create Sub Class Instance And Display Father's Property

s = Son()
s.display_property()
