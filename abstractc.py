# Python Program To Create Abstract Class And Sub Classes 
# Which Implement The Abstract Method Of The Abstract Class

'''
Function Name    :  Abstract Class
Function Date    :  20 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

from abc import ABC, abstractmethod
class Myclass(ABC):
    @abstractmethod
    def calculate(self, x):
        pass # Empty Body, No Code
    
# This Is Sub Class Of Myclass

class Sub1(Myclass):
    def calculate(self, x):
        print('square value = ', x*x)

# This Is Another Sub Class For Myclass

import math
class Sub2(Myclass):
    def calculate(self,x):
        print('square root = ', math.sqrt(x))
        
# Third Sub Class For Myclass

class Sub3(Myclass):
    def calculate(self, x):
        print('Cube value = ', x**3) 
        
# Create Sub1 Class Object And Call Calculate() Method

obj1 = Sub1()
obj1.calculate(16)

# Create Sub2 Class Object And Call Calculate() Method

obj2 = Sub2()
obj2.calculate(16)

# Create Sub3 Class Object And Call Calculate() Method

obj3 =Sub3()
obj3.calculate(16)

       