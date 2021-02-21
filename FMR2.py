'''
Description      :  Creating Filter, Map, Reduce And Get The List Elements From User 
                    & Display The Elements & Perform Addition Of That List Elements
Function Date    :  21 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''


from functools import reduce


def CheckEven(no):
    
    if no % 2 == 0: # we can use return (no % 2)
        return True
    else:
        return False

def Increment(no):
    return no + 2

def Add(no1, no2):
    return no1 + no2


def main():

    arr = []
    print("Enter Number Of Elements : ")
    size = int(input())

    for i in range(size):
        print("Enter Elements Number : ", i + 1)
        no = int(input())
        arr.append(no)

    print("Your Entered Data Is : ", arr)
    newdata = list(filter(CheckEven, arr)) # newdata = MarvellousFilter(arr)
    print("After Filtering Data Is : ", newdata)    

    newdata1 = list(map(Increment, newdata))#newdata1 = MarvellousMap(newdata)
    print("After Map Is : ", newdata1)

    output = reduce(Add, newdata1)#output = MarvellousReduce(newdata1)
    print("After Reduce Result Is : ", output)    
    

if __name__ == "__main__":
    main()