'''
Description      :  Creating Decorator Explicitly
Function Date    :  14 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''


#inbuilt function from module

def Subtraction(no1, no2):
    return no1 - no2

def SubDecorator(func_name):
    def Updator(a, b):
        if a < b: # first parameter is small
            temp = a
            a = b
            b = temp
        return func_name(a,b)

    return Updator

def main():

    sub = SubDecorator(Subtraction) # subtraction is the object

    print("Enter first number ")
    value1 = int(input())

    print("enter second value ")
    value2 = int(input())

    ret = sub(value1,value2)
    
    print("Subtraction is ", ret)

if __name__ == "__main__":
    main()