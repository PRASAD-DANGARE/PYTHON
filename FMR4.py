'''
Description      :  Directly Using Filter, Map, Reduce In Lambda
Function Date    :  21 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

import functools 

def main():

    arr = []
    print("Enter Number Of Elements : ")
    size = int(input())

    for i in range(size):
        print("Enter Elements Number : ", i + 1)
        no = int(input())
        arr.append(no)

    print("Your Entered Data Is : ", arr)

    newdata = list(filter(lambda no: (no % 2 == 0), arr)) # newdata = MarvellousFilter(arr)
    print("After Filtering Data Is : ", newdata)    

    newdata1 = list(map(lambda no: no + 2, newdata))#newdata1 = MarvellousMap(newdata)
    print("After Map Is : ", newdata1)

    output = functools.reduce(lambda no1, no2: no1 + no2, newdata1)#output = MarvellousReduce(newdata1)
    print("After Reduce Result Is : ", output)    
    

if __name__ == "__main__":
    main()