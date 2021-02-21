'''
Description      :  Creating Filter, Map, Reduce Explicitly 
Function Date    :  21 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

# Filter Map Reduce 


def CheckEven(no):

    if no % 2 == 0:
        return True
    else:
        return False

def MarvellousFilter(arr):
    brr = []
    
    for i in range(len(arr)):
        if CheckEven(arr[i]) == True:
            brr.append(arr[i])
    
    return brr

def MarvellousMap(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] + 2

    return arr

def MarvellousReduce(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]

    return sum

def main():
    
    arr = []
    print("Enter Number Of Elements : ")
    size = int(input())

    for i in range(size):
        print("Enter Elements Number : ", i + 1)
        no = int(input())
        arr.append(no)

    print("Your Entered Data Is : ", arr)
    newdata = MarvellousFilter(arr)
    print("After Filtering Data Is : ", newdata)    

    newdata1 = MarvellousMap(newdata)
    print("After Map Is : ", newdata1)

    output = MarvellousReduce(newdata1)
    print("After Reduce Result Is : ", output)    
    
if __name__ == "__main__":
    main()
