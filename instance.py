# Python Program To Store Data Into Instance Using Mutator Method 
# And To Retrieve Data From The Instance Using Accessor Method

'''
Function Name    :  Accessor And Mutator Method.
Function Date    :  17 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

class Student:
    # Mutator Method
    
    def setName(self, name):
        self.name = name
        
    # Accessor Method
    
    def getName(self):
        return self.name
    
    # Mutator Method
    
    def setMarks(self, marks):
        self.marks = marks
    
    # Accessor Method
    
    def getMarks(self):
        return self.marks
        
# Create Instance With Some Data From Keyboard

n = int(input('\n How Many Students ? '))

i = 0
while(i<n):
    
    # Create Student Class Instance
    
    s = Student()
    name = input('\n Enter Name : ')
    s.setName(name)
    marks = int(input('Enter Marks : '))
    s.setMarks(marks)
    
    # Retrieve Data From Student Class Instance
    
    print('\n Hi', s.getName())
    print('\n Your Marks', s.getMarks())
    
    i += 1
    print('--------------------------')
    
    