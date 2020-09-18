# Python Program To Access Base Class Constructor And Method In The Sub Class Using super()

'''
Function Name    :  Access Base Class Constructor And Method In Sub Class
Function Date    :  18 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''


class Square:
    def __init__(self, x):
        self.x = x
        
    def area(self):
        print('\n Area Of Square = ', self.x*self.x)
        
class Rectangle(Square):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
        
    def area(self):
        super().area()
        print('Area Of Rectangle = ', self.x*self.y)
        print("\n")
        
# Find Area Of Square And Rectangle

a, b = [float(x) for x in input("\n Enter Two Measurments In Space : ").split()]
r = Rectangle(a, b)
r.area()

