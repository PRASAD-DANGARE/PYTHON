'''
Description      :  Creating Module For Addition Of Two Numbers  
                 :  This File Contain Entry Point Function For module2.py
Function Date    :  07 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''

import module2

def main(): # indentation 0 , we can give any name

    no1 = int(input("enter first number ")) # 1
    no2 = int(input("enter second number ")) # 2
    ans = module2.Addition(no1, no2) # function call 3

    print ("addition is : ", ans) 

    no1 = int(input("enter first number "))
    no2 = int(input("enter second number "))
    ans = module2.Addition(no1, no2) # function call

    print ("addition is : ", ans)

#print(__name__) # here display the message main, entry point function

if __name__ == "__main__": # indentation 0
    main()