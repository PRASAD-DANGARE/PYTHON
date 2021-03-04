'''
Description      :  Demonstration of __init__, __del__ (Constructor, Destructor)
Function Date    :  04 Mar 2021
Function Author  :  Prasad Dangare

'''

class Demo:
    x = 10 # class variable
    y = 20 # class variable
    def __init__(self):
        print("Inside Consrtuctor")
        self.i = 30 # instance variable
        self.j = 40 # instance variable

    def __del__(self): # del is the method
        print("Inside Destructor")

    def Fun(self):
        print("Inside Fun")

def main():
    obj1 = Demo()
    obj2 = Demo()

    obj1.Fun() # fun(obj1) fun(1000)
    obj2.Fun() # fun(obj2) fun(2000)

    del obj1 # del is the keyword
    del obj2

    #obj1.Fun() error because object get deleted
if __name__ == "__main__":
    main()