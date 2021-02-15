'''
Description      :  Use Of Forloop With Hardcoded Value
Function Date    :  15 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  str

'''

def display():
    print("Output of For loop")
    icnt = 0
    for icnt in range(10, 1, -1):
        print(icnt)
    else:
        print("End of For loop")

def main():
    display()

if __name__ == "__main__":
    main()