'''
Description      :  Demonstration Of Super Keyword 
Function Date    :  08 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

class Base:

    def __init__(self):
        self.i = 10
        self.j = 20

    def fun(self):
        print("Base Fun")
    
class Derived(Base):

    def __init__(self):
        Base.__init__(self)
        # self.__init__() not allowed recursive call
        # super().__init__() not allowed
        self.x = 30
        self.y = 40

    def gun(self):
        print("Derived gun")
        Base.fun(self)
        self.fun() # fun(self)
        super().fun() # fun(self)
        # print(i) not allowed
        print(self.i)
        # print(super().i) not allowed

dobj = Derived()
dobj.gun()
