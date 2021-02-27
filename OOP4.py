'''
Description      :  Object Orientation With Flow 
Function Date    :  27 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''

class Arithmatic: # Class Defination
    value = 111 # class variable

    def __init__(self, i, j): # Class Constructor 
        print("Inside Constructor")
        self.no1 = i # characteristics
        self.no2 = j # Instance Variable 
    
    def Add(self): # Instance Method
        print(Arithmatic.value)
        return self.no1 + self.no2

    def Sub(self): # Instance Method
        return self.no1 - self.no2

def main():

    print("Value Is : ", Arithmatic.value)

    obj1 = Arithmatic(21, 11) # __init__(obj1, 21, 11)
    obj2 = Arithmatic(101, 51) # __init__(obj2, 101, 51)
    print("Value is : ", obj1.value)

    ret = obj1.Add() # ret = Add(obj1)
    print("Addition is ", ret)
    ret = obj1.Sub() # ret = sub(obj1)
    print("Subtraction is ", ret)

    ret = obj2.Add() # ret = Add(obj2)
    print("Addition is ", ret)
    ret = obj2.Sub() # ret = sub(obj2)
    print("Subtraction is ", ret)


if __name__ == "__main__":
    main()