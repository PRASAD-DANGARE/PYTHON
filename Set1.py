'''
Function Name    :  main()
Description      :  Performing Various Inbuilt Methods On Set
Function Date    :  14 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''


def main():

    arr = {10,20.5, "Hello",10}

    print(type(arr))
    print(arr)

    print(len(arr))

    for value in arr:
        print(value)

    if "Hello" in arr:
        print("Hello is there")

    arr.add(20)
    print(arr)

    #arr.remove(120) # it gives error (key error)if element is not in the set
    #print(arr)

    arr.discard(120) # it ignore it if value is not in the set
    print(arr)

    #arr.pop() dont do this in set 
    #print(arr)

if __name__ == "__main__":
    main()

# set is also consider as dictionary without value