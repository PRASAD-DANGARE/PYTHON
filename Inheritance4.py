'''
Description      :  Multiple Inheritance 
Function Date    :  06 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

class Base1:

    def __init__(self):
        print("Inside Base1 Constructor")

    def fun(self):
        print("Base1 fun")

class Base2:
    def __init__(self):
        print("Inside Base2 constructor")
    def fun(self):
        print("Base2 fun")

class Derived(Base2, Base1):
    def __init__(self):
        Base2.__init__(self)
        Base1.__init__(self)
        print("Inside Derived Constructor")

def main():
    
    dobj = Derived()
    dobj.fun()

if __name__ == "__main__":
    main()