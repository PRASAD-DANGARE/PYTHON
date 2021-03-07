'''
Description      :  Single Level Inheritance 
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

    def Fun(self):
        print("Inside Base Fun")

    def Gun(self):
        print("Inside Base Gun")

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        self.x = 30
        self.y = 40
        print("Inside Derivd Constructor")
        
    def Sun(self):
        print("Inside Derived Sun")

    def Gun(self):  # overriding
        print("Inside Derived Gun")

def main():
    
    bobj = Base() # object of base class
    print(bobj.i)
    print(bobj.j)

    bobj.Fun()
    bobj.Gun()

    dobj = Derived()
    print(dobj.i)
    print(dobj.j)
    print(dobj.x)
    print(dobj.y)

    dobj.Sun()
    dobj.Gun()
    dobj.Fun()

if __name__ == "__main__":
    main()