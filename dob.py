# Python Program To Create Dob Class Within Person Class

'''
Function Name    :  Create Date Of Birth Within Person Class
Function Date    :  17 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String,Integer
'''

class Person:
    def __init__(self):
        self.name = 'Prasad'
        self.db = self.Dob()
        
    def display(self):
        print('Name = ', self.name)
            
        # This Is Inner Class
        
    class Dob:
        def __init__(self):
            self.dd = 9
            self.mm = 3
            self.yy = 2002
        def display(self):
            print('Dob = {}/{}/{}'.format(self.dd, self.mm, self.yy))

# Creating Person Class Object

p = Person()
p.display()

# Create Inner Class Object

x = p.db
x.display()                