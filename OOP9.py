'''
Description      :  Class Variable, Instance Variable, Instance Method, Destructor 
Function Date    :  06 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

class Marvellous:

    Value1 = 11 # class / static characteristics

    def __init__(self, no1, no2): # constructor
        self.i = no1 # instance variable
        self.j = no2 
        print("Inside Constructor")
    
    def __del__(self): # Destructor
        print("Inside Destructor")

    def Fun(self): # instance method 
        print("Inside Fun Method")
        print("Value of j is", self.j)

def main():
    
    obj1 = Marvellous(11,21)
    obj2 = Marvellous(51, 101)

    print("Value of i from obj1 ", obj1.i) # Accessing instance members
    print("Value of i from obj2 ", obj2.i)
    print("Value of Class member ", Marvellous.Value1) # Accessing class members

    obj1.Fun() # calling instance method
    obj2.Fun()

    del obj1 # deallocating the memory of object
    del obj2

if __name__ == "__main__":
    main()