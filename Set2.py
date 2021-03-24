'''
Function Name    :  main()
Description      :  Demonstration Of Set
Function Date    :  14 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

def main():

    arr = {10,20,30,40}

    print(type(arr))

    temp = list(arr)

    print(type(temp))

    temp[1] = 21 # type conversion

    arr = set(temp)

    print(arr)

if __name__ == "__main__":
    main()