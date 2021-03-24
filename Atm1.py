'''
Function Name    :  ATM(), Deposit()
Description      :  Accept Amount From User & Perform Deposit, Withdraw With Sincronization
Function Date    :  14 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

# with sincronization the program is not terminated eg withdraw and deposit at same time on joint account 
# for that we have to use locking system (acquire, release) so at a time one condition can run and other is waiting

import threading

Amount = 1000

def ATM(func, kulup):
    func(kulup)

def Deposit(kulup):
    kulup.acquire()
    value = int(input("Enter the amount to deposit : "))
    global Amount
    Amount = Amount + value
    print("Deposit succesful - Balance : ",Amount)
    kulup.release()
    
def Withdraw(kulup):
    kulup.acquire()
    value = int(input("Enter the amount to withdraw : "))
    global Amount
    if value > Amount:
        print("There is no sufficeient balance : ")
    else:
        Amount = Amount - value
        print("Withdraw succesful - Balance : ",Amount)
    kulup.release()

def main():
    print("Inside main")
    
    kulup = threading.Lock()
    
    t1 = threading.Thread(target = ATM, args = (Deposit,kulup,))
    t2 = threading.Thread(target = ATM, args = (Withdraw,kulup))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("ATM application closed")

if __name__ == "__main__":
    main()
