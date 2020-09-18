# Python Program To Use The Teacher Class

'''
Function Name    :  Using Teacher Class teacher.py In This Program teacher2.py  
Function Date    :  18 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

# Save This Code As teacher2.py
# Using Teacher Class 

from teacher import Teacher

# Create Instance

t = Teacher()

# Store Data Into Instance

t.setid(10)
t.setname('Prasad')
t.setaddress('Sanjuda Complex, 412308, Papadewasti, Pune ')
t.setsalary(25000.50)

# Retrieve Data From Instance And Display

print('\n Id = ', t.getid()) 
print('Name = ', t.getname())
print('Address = ', t.getaddress())
print('Salary = ', t.getsalary())
print("\n")
