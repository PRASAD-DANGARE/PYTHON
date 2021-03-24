'''

class Name       :  Student
Function Name    :  __eq__(), __gt__()
Description      :  Demonstration Of Operator Overloading
Function Date    :  15 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

class Student:

    def __init__(self, str, a, b, c):
        self.name = str
        self.m1 = a
        self.m2 = b
        self.m3 = c

    def __eq__(self, other):
        return ((self.m1 == other.m1) and (self.m2 == other.m2) and (self.m2 == other.m3))
        
    def __gt__(self, other):
        return ((self.m1 > other.m1) and (self.m2 > other.m2) and (self.m2 > other.m3))
    
def main():
    obj1 = Student("Prasad", 70, 91, 80)
    obj2 = Student("Sarvesh", 56, 90, 78)
    
    if obj1 == obj2:
        print("Both The Students Are Same")
    else:
        print("Both The Student Are different")

    if obj1 > obj2:
        print("First Object is greater")
    else:
        print("Second object is greater")

if __name__ == "__main__":
    main()