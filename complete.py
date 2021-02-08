'''
Description      :  Performing Addition & Subtraction 
Function Date    :  08 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''


# defination of addition function

def Addition(no1, no2):
    ans = no1 + no2
    return ans

# defination of Subtraction function

def Subtraction(no1, no2):
    ans = no1 - no2
    return ans

# entry point function

def main(): 
    print ("Enter first number : ")
    value1 =  int(input())

    print ("Enter second number : ")
    value2 =  int(input())

    ret1 = Addition(value1, value2)
    ret2 = Subtraction(value1, value2)

    print("Addition is : ", ret1)
    print("subtraction is : ", ret2)

# code starter
if __name__ == "__main__": # __name__ is name of the module (file name) when we print it
    main()
