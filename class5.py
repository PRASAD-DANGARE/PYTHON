# Python Program To Create Emp Class 
# And Make All The Members Of The Emp Class Available To Another Class ie. Myclass

'''
Function Name    :  This Class Contain Employee Details.
Function Date    :  17 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String,Integer
'''

class Emp:
    # This Is A Constructor
    
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
        
    # This Is An Instance Method
    
    def display(self):
        print('Id = ', self.id)
        print('Name = ', self.name)
        print('Salary = ', self.salary)
        
# This Class Display Employee Details

class Myclass:
    
    # Method To Receive Emp Class Instance
    # And Display Employee Details
    
    @staticmethod
    def mymethod(e):
        
        # Increment Salary Of e By 1000
        
        e.salary+=1000;
        e.display()
        
# Create Emp Class Instance e

e = Emp(10, 'Prasad Dangare', 7057.75)

# Call Static Method Of Myclass And Pass e

Myclass.mymethod(e)
