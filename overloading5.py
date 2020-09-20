# Python Program To Overide The Super Class Method In Sub Class

'''
Function Name    :  Overide The Super Class Method In Sub Class
Function Date    :  20 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import math
class Square:
    def area(self, x):
        print('square area = %.4f'% x*x)
        
class Circle(Square):
    def area(self, x):
        print('Circle Area = %.4f'% (math.pi*x*x))
        
# call area() Using Sub Class Object

c = Circle()
c.area(15)
