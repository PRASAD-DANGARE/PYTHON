'''
Function Name    :  main()
Description      :  Exception Handling using except block
Function Date    :  21 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

def main():

    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    try:
        ans = no1 / no2
    
    except ZeroDivisionError as obj:
        print("Divide by zero exception", obj)
        
    except Exception as eobj:
        print("Exception Occurs", eobj)

    else:

        print("Division is : ", ans)

if __name__ == "__main__":
    main()