'''
Description      :  Lambda Function Which Accept 2 Number And Perform Addition
Function Date    :  21 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''


def Addition(iNo1, iNo2):
    return iNo1 + iNo2

Sum = lambda iNo1, iNo2 : iNo1 + iNo2 # Sum is reference of the object and we can give this object to other function
                                      # eg salon, mri machine

def fun(name):
    ret = name(10, 20)
    print("Value From Fun is ", ret)
def main():

    print("Enter One Number : ")
    value1 = int(input())

    print("Enter Second Number : ")
    value2 = int(input())

    ret = Addition(value1, value2)
    print("Addition Is : ", ret)

    ret = Sum(value1, value2)
    print("Addition With Lambda  : ", ret)

    fun(Sum) # we pass the object, is is also like inline in c++

if __name__ == "__main__":
    main()