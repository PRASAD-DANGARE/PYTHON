# Python Program To Showing Inheritance In Which Two Sub Classes Are Derived From Base Class

'''
Function Name    :  Inheritance Which Two Sub Classes Are Derived From Base Class
Function Date    :  18 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

class Bank(object):
    cash = 1000000
    @classmethod
    def available_cash(cls):
        print(cls.cash)
        
class MaharashtraBank(Bank):
    pass

class StateBank(Bank):
    cash = 2000000
    @classmethod
    def available_cash(cls):
        print(cls.cash + Bank.cash)
        
a = MaharashtraBank()
a.available_cash()

s = StateBank()
s.available_cash()
