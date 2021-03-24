'''

class Name       :  Demo
Function Name    :  __add__()
Description      :  Demonstration Of Operator Overloading V2
Function Date    :  15 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

class Demo:

    def __init__(self, x, y):
        self.i = x
        self.j = y

    def __add__(self, other):
        return Demo(self.i + other.i, self.j + other.j)

def main():
    #no1 = 10
    #no2 = 20

    obj1 = Demo(10,20)
    obj2 = Demo(30,40)

    ret = obj1 + obj2

    print(ret.i, ret.j)

    #print(obj1)
    #print(obj2)
    #ret = no1 + no2
    #print("Addition is : ", ret)

if __name__ == "__main__":
    main()