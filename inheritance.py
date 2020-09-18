# Python Program To Access The Base Constructor From Sub Class

'''
Function Name    :  Access Base Constructor From Sub Class
Function Date    :  18 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

class Father:
    def __init__(self):
        self.property = 10000000.00
        
    def display_property(self):
        print('Father\'S property= ', self.property)
        
class Son(Father):
    pass # We Do Want To Write Anything In The Sub Class

# Create Sub Class Instance And Display Father's Property

s = Son()
s.display_property()
