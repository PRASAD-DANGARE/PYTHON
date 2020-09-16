# Python Program To Define Student Class And Create An Object To It
#  Also We Will Call The Method And Display The Student Details

'''
Function Name    :  Define Student Class And Create An Object To It.
Function Date    :  16 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

# This Is An Instance Variable

class Student: # Class Student (objects):
    
    # This Is A Special Method Called Constructor
    
    def __init__(self):
        self.name = 'Prasad'
        self.age = 18
        self.marks = 100
        
# This Is An Instance Method
    
def talk(self):
    print('Hi, I Am ', self.name)
    print('My Age Is ', self.age)
    print('My Marks Are ', self.marks)
        
# create an instance to student class
    
s1 = Student() 
    
# call the method using the instance
    
s1.talk()
    