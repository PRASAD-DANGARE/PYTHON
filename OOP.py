'''
Description      :  Demonstration Of Object Orientation 
Function Date    :  27 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''

print("Demonstration of Class")

class Demo: # Class Defination

    def __init__(self,value1,value2): # Class Constructor
        print("Inside init method")
        self.i = value1 # Characteristics
        self.j = value2 # Instance Variable

    def fun(self): # Instance Method
        print("Inside fun")
        print(self.i,self.j)

    def Add(self):
        print(self.i + self.j)

# Create object of Demo class

obj1 = Demo(10,20) # __init_(obj1, 10, 20) like that the call goes 

obj1.fun() # Call the method fun

obj2 = Demo(50,60) # Create object of Demo class

obj2.fun() # Call the method fun

obj1.Add() # Call method Add to perform addition of characteristics
obj2.Add()