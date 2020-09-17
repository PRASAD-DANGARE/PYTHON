# Python Program To Create A Bank Class Where Deposits And Withdrawals Can Be Handled By Using Instance Methods

'''
Function Name    :  Class Handle Deposits And Withdrawals In Bank.
Function Date    :  17 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String,Integer
'''

import sys
class Bank(object):

    """ Bank Related Transactions """
    
    # To Initialize Name And Balance Instance Vars
    
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
        
    # To Add Deposit Amount To Balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
        
    # To Deduct Withdrawal Amount From Balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            print('\n Balance Amount Is Less, So No Withdrawal.')
        else:
            self.balance -= amount
        return self.balance
    
# Using The Bank Class
# Create An Amount With The Given Name And Balance
    
name = input('\n Enter Account Holder Name : ')
b = Bank(name) # This Is Instance Of Bank Class
    
# Repeat Continuously Till Choice Is 'e' Or 'E'
    
while(True):
    print('\n d -Deposit, w -Withdraw, e -Exit')
    choice = input('\n your choice : ')
    if choice == 'e' or choice == 'E':
        sys.exit()
        
    # Amount For Deposit Or Withdraw
    
    amt = float(input('\n Enter Amount : '))
        
    # Do The Transaction
    
    if choice == 'd' or choice =='D':
        print('\n Balance After Deposit : ', b.deposit(amt))
    elif choice == 'w' or choice == 'W':
        print('\n Balance After Withdrawal : ', b.withdraw(amt))
