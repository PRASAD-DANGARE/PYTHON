# Python Program To Overload The Multiplication Operator To Make It Act On Objects

'''
Function Name    :  Overload Multiplication Operator On Object
Function Date    :  20 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def __mul__(self, other):
        return self.salary*other.days
    
class Attendance:
    def __init__(self, name, days):
        self.name = name
        self.days = days
        
x1 = Employee('Prasad', 500.00)
x2 = Attendance('Prasad', 25)
print('This Month Salary = ', x1*x2)
