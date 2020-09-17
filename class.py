# Python Program Using A Student Class With Instance Methods To Process The Data Of Several Students

'''
Function Name    :  Instance Method To Process Data Of The Objects.
Function Date    :  17 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

class Student:
    # This Is A Constructor
    
    def __init__(self, n = '', m = 0):
        self.name = n
        self.marks = m
        
    # This Is An Instance Method
    
    def display(self):
        print('\n Hi', self.name) 
        print('Your Marks', self.marks)
        
    # To Calculate Grades Based On Marks
    
    def calculate(self):
        if(self.marks >= 100):
            print('\n You Got First Grade')
        elif(self.marks >= 60):
            print('\n You Got Second Grade')
        elif(self.marks >= 50):
            print('\n You Got Third Grade')
        else:
            print('\n You Are Failed')
            
# Create Instance With Some Data From Keyboard

n = int(input('\n How Many Students ? '))

i = 0
while(i<n):
    name = input('\n Enter Name : ')
    marks = int(input('Enter Marks : '))
    
    # Create Student Class Instance And Store Data
    
    s = Student(name, marks)
    s.display()
    s.calculate()
    i += 1
    print('---------------------')
     