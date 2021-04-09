'''
Function Name    :  main()
Description      :  Exception Handling using finally block
Function Date    :  21 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

def main():

    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    try:
        print("Inside try")
        ans = no1 / no2
    
    except ZeroDivisionError as obj:
        print("Divide by zero exception", obj)

    else:
        print("Insidee else")
        print("Division is : ", ans)

    finally:
        print("Inside finally")
        print("Deallocate all the resources")

if __name__ == "__main__":
    main()