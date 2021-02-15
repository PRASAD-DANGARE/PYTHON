'''
Description      :  Accept Elements From User And Display The List With, Display Addition Of The List Elements
Function Date    :  15 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

def Addition(LIST):
    sum = 0
    for i in range(len(LIST)):
        sum = sum + LIST[i]
    return sum

def main():
    arr = []
    print("enter the number elements")
    size = int(input())

    for i in range(size):
        print("Enter the elements no : ", i + 1)
        value = int(input())
        arr.append(value)

    print("Accepted Data is : ", arr)

    ret = Addition(arr)

    print("Addition of all elements is : ", ret)

if __name__ == "__main__":
    main()