'''
Description      :  Demonstration Of Recursion With for, while Loop
Function Date    :  22 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

def DisplayIF(no): # Forloop Iteration

    for i in range(no): 
        print("Hello")

def DisplayIW(no): # whileloop Iteration
    while no != 0:
        print("Welcome")
        no = no -1

# Recursion : Calling the function from same function itself

def DisplayR(no): # Recursion Iteration
    if no != 0:
        no = no -1
        print("Hii")
        DisplayR(no)

def main():

    value = int(input("Enter Number Of Iterations : "))

    print("Calling Iterative Function With For Loop")
    DisplayIF(value)

    print("Calling Recursion Function")
    DisplayR(value)

    print("Calling Iterative Function With While Loop")
    DisplayIW(value)

if __name__ == "__main__":
    main()