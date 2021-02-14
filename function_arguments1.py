'''
Description      :  Types Of Function Arguments
Function Date    :  14 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Str
'''

# positional arguments

def Students(name, rno, address, marks):
    print("Name is :", name)
    print("Roll Number is :", rno)
    print("Address is :", address)
    print("Marks is :", marks)

# Keyword arguments

def Computer(Ram, Processor, HDD):
    print("Ram Size is :", Ram)
    print("Processor Name is :", Processor)
    print("Size of HDD Is :", HDD)

# Default arguments (Should be from right to left order)

def CircleArea(Radious, PI = 3.14):
    print("Value of PI is :", PI)
    return PI * Radious * Radious

# Variable number of arguments

def Fun(*value):
    print("Number Of Arguments Are : ", len(value))

# Function Call For the above

def main():
    Students("Prasad", 11, "Hadpsar Pune", 56)
    print("\n")

    Computer(Processor = "i7", Ram = 8, HDD = "1TB")
    print("\n")
    Computer(Ram = 16, HDD = "512GB", Processor = "i5")
    print("\n")

    CircleArea(10.25)
    CircleArea(10.25, 7.12)
    CircleArea(Radious = 10.25, PI = 7.12)
    print("\n")

    Fun(10,20,30,40)
    Fun(10,20,30,40,50)
    Fun()

if __name__ == "__main__":
    main()





