'''
Description      :  Input In Function By .format Method
Function Date    :  14 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''

# defination of function, use of .format method

def Addition(no1, no2):
    ans = no1 + no2
    return ans

def main():
    print("enter first number")
    value1 = int(input())

    print("enter second number")
    value2 = int(input())

    ret = Addition(value1, value2)
    print("Addition of {} and {} is {} ".format(value1, value2, ret))

if __name__ == "__main__":
    main() 