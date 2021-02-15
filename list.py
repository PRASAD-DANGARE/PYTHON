'''
Description      :  Use Of Range Type
Function Date    :  15 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

def display(list):
    icnt = 0
    for icnt in range(len(list)):
        print(list[icnt])

def main():
    arr = [10,20,30,40,50]
    display(arr)

    brr = [10, "Marvellous", 59.70, "Pune"]
    print(brr)

if __name__ == "__main__":
    main()