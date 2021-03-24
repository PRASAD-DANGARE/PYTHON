'''
Function Name    :  ATM(), Deposit()
Description      :  Accept Amount From User & Perform Deposit, Withdraw Without Sincronization
Function Date    :  14 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

# without sincronization the program is terminated eg withdraw and deposit at same time on joint account  

import threading

Amount = 1000

def ATM(func):
    func()

def Deposit():

    value = int(input("Enter the amount to deposit : "))
    global Amount
    Amount = Amount + value
    print("Deposit Succesful - Balance : ", Amount)

def Withdrwa():

    value = int(input("Enter the amount to withdrwa : "))
    global Amount
    if value > Amount:
        print("There is no sufficient balance")
    else:
        Amount = Amount - value
        print("Withdraw succesful - balance : ", Amount)

def main():

    print("Inside Main")
    ATM(Deposit)
    ATM(Withdrwa)

if __name__ == "__main__":
    main()