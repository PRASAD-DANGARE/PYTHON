# Python Program That Uses The Function Of Employee Module 
# And Calculate The Gross And Net Salaries Of An Employee

'''
Function Name    :  Create Our Own Module.
Function Date    :  9 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

""" Please Use employee2.py With employee.py Becaues We Create Our Own Module """
""" When We Compile employee2.py We Use Content Of employee.py Such As (da,hra,pf,itax)"""


from employee import*

# Calculate Gross Salary Of Employee By Taking Basic

basic = float(input('Enter Basic Salary Again : '))
print("\n")

# Calculate Gross Salary

gross = basic+da(basic)+hra(basic)
print('Your Gross Salary : {:10.2f}'.format(gross))
print("\n")

# Calculate Net Salary

net = gross - pf(basic)-itax(gross)
print('Your Net Salary : {:10.2f}'.format(net))
print("\n")