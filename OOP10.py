'''
Description      :  Use Of Decorator 1) Class Method, 2) Static Mthod 
Function Date    :  06 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''


class Student:
    School = "Abhinav"  

    def __init__(self, no1, no2, no3):
        self.m1 = no1
        self.m2 = no2
        self.m3 = no3

    def Instance_Total(self): # instance method
        print("Inside Instance Method")
        return self.m1 + self.m2 + self.m3

    @classmethod # Decorator
    def Class_DisplaySchool(cls): # class method
        print("School Name is : ",cls.School)

    @staticmethod # Decorator
    def Static_Info():  # static method
        print("This class contains the information of school")

def main():

    Student.Class_DisplaySchool() # calling class method
    obj1 = Student(50,80,70) # object creation
    obj2 = Student(65,80,75)
    ret = obj1.Instance_Total() # calling instance method
    print("Total obtained marks", ret)
    Student.Static_Info() # calling static method

if __name__ == "__main__":
    main()