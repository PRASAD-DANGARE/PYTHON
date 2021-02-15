'''
Description      :  Display N Number Of Iteration From User  
Function Date    :  15 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  str

'''

def Startdynamic(No):
    icnt = 0
    while icnt < No:
        print("Jay Ganesh")
        icnt = icnt + 1

def main():
    print("Enter Number Of Iterations")
    Value = int(input())

    Startdynamic(Value)

if __name__ == "__main__":
    main()