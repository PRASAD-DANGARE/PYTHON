# Python Program To Understand That Myclass Method Is Shared By All Of Its Objects


'''
Function Name    :  Myclass Method Is Shared By All Of Its Objects
Function Date    :  20 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

class Myclass:
    def calculate(self, x):
        print('Square Value = ', x*x)
        
# All Objects Share Same Calculate() Method

obj1 = Myclass()
obj1.calculate(2)

obj2 = Myclass()
obj2.calculate(3)

obj3 = Myclass()
obj3.calculate(4)


