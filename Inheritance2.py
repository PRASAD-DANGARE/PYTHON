'''
Description      :  Multi Level Inheritance 
Function Date    :  06 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

class Base:

    def __init__(self):
        self.i = 10
        self.j = 20
        print("Inside Base Constructor")

class Derived1(Base):
    def __init__(self):
        Base.__init__(self)
        self.x = 30
        self.y = 40
        print("Inside Derived1 Constructor")

class Derived2(Derived1):
        def __init__(self):
            Derived1.__init__(self)
            self.a = 50
            self.b = 60
            print("Inside Derived2 Constructor")
        
def main():
    
    dobj = Derived2()  # created object of Derived2 class
    print(dobj.i)
    print(dobj.j)
    print(dobj.x)
    print(dobj.y)
    print(dobj.a)
    print(dobj.b)

if __name__ == "__main__":
    main()