'''
Description      :  Demonstration of Characteristics of Class
Function Date    :  04 Mar 2021
Function Author  :  Prasad Dangare

'''

print("Demonstration of Characteristics of Class")

class Demo: # Class Defination
    x = 50 # Class Variable

    def __init__(self,no1,no2): # Class Costructor
        self.i = no1 # Instance Variable / Characteristics
        self.j = no2


obj1 = Demo(10,20) # Object Created For Characteristics
obj2 = Demo(11,21)

# i & j Are Instance Variable

print(obj1.i) # 10
print(obj1.j) # 20

print(obj2.i) # 11
print(obj2.j) # 21

print(Demo.x) # 50 No Need To Create Object We Can Directly Access It By Its Class Name