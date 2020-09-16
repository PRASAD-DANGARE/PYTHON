# Python Program To Create Student Class With A Constructor Having More Than One Parameter

'''
Function Name    :  Create Student Class With A Constructor More Than One Parameter.
Function Date    :  16 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

class Student:
    
    # This Is Constructor
    def __init__(self, n = '.',m=0):
        self.name = n
        self.marks = m
        
    # This Is An Instance Method
    
    def display(self):
        print('Hi', self.name)
        print('Your Marks', self.marks)
        
# Constructor Is Called Without Any Arguments

s = Student()
s.display()
print('----------------')

# Constructor Is Called With 2 Arguments

s1 = Student('Prasad Dangare', 93)
s1.display()
print('----------------')