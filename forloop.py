'''
Description      :  Use Of Forloop With Whileloop  
Function Date    :  15 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  str

'''

def displayf(value):
    print("output of for loop")
    icnt = 0
    for icnt in range(0, value):
        print("Jay Ganesh")

def displayw(value):
    print("output of while loop")
    icnt = 0
    while icnt < value:
        print("jay ganesh")
        icnt = icnt + 1

def main():
    print("enter the number of iteration")
    no = int(input())

    displayf(no)
    displayw(no)

if __name__ == "__main__":
    main()

'''

range (start, end, step) start -> starting point of the sequence(exclusive)
                         step -> increment factor of the sequence default is 1
                         end -> value for the sequence

range(1,5,1) -> 1 2 3 4
range(10) -> 0 1 2 3 4 5 6 7 8 9
range(1,10,2) -> 1 3 5 7 9
'''
