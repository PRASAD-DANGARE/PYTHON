# Python Program To Pickle Emp Class Objects

'''
Function Name    :  Pickle Emp Class Objects
Function Date    :  25 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

import Emp, pickle

# Open emp.dat File As A Binary File For Writing

f = open('emp.dat', 'wb')
n = int(input('How Many Employees? '))

for i in range(n):
    id = int(input('Enter Id : ')) 
    name = input('Enter Name : ')
    sal = float(input('Enter Salary : '))
    
    # Create Emp Class Object
    
    e = Emp.Emp(id, name, sal)
    
    # Store The Object e Into The File f
    
    pickle.dump(e, f)
    
# Close The File

f.close()
