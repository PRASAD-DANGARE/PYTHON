# Python Program To Calculate The Gross Salary And Net Salary Of An Employee


'''
Function Name    :  Calculate Gross Salary And Net Salary Of An Employee.
Function Date    :  9 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

def da(basic):
    """ da Is 80% Of Basic Salary """
    
    da = basic*80/100
    return da

# To Calculate House Rent Allowance

def hra(basic):
    """ hra Is 15% Of Basic Salary """
    
    hra = basic*15/100
    return hra

# To Calculate Provident Fund Amount

def pf(basic):
    """ pf Is 12% Of Basic Salary"""
    
    pf = basic*12/100
    return pf

# To Calculate Income Tax Payable By Employee

def itax(gross):
    """ tax Is Calculated At 10% On Gross """
    
    tax = gross*0.1
    return tax

# This Is The Main Program
# Calculate Gross Salary Of Employee By Taking Baisc

basic = float(input('\n Enter Basic Salary : '))
print("\n")

# Calculate Gross Salary

gross = basic+da(basic)+hra(basic)
print('Your Gross Salary : {:10.2f}'.format(gross))
print("\n")

# Calculate Net Salary

net = gross - pf(basic)-itax(gross)
print('Your net Salary : {:10.2f}'.format(net))
print("\n")

  