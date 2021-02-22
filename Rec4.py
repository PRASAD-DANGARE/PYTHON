'''
Description      :  Demonstration Of Recursion But Set The Variable As Global
Function Date    :  22 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

def AdditionF(data):
    sum = 0
    for i in range(len(data)): 
        sum = sum + data[i]
    return sum


def AdditionW(data):
    sum = 0
    i = 0
    while i < len(data):
        sum = sum + data[i]
        i = i + 1
    return sum

sum = 0
i = 0
def AdditionR(data):
    global sum
    global i
    if i < len(data):
        sum = sum + data[i]
        i = i + 1
        AdditionR(data)
    return sum

def main():
    arr = []
    size = int(input("Enter the size of array"))
    for i in range(size): arr.append(int(input()))

    print("data is : ", arr)

    print("addition is ", AdditionF(arr))

    print("addition is ", AdditionW(arr))

    print("addition is ", AdditionR(arr))


if __name__ == "__main__":
    main()