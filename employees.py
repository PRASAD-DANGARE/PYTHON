# Python Program To Create A List With Employee Data And Then Retrieve A Particular Details

'''
Function Name    :  Find Details Of An Particular Employee .
Function Date    :  10 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer,String
Output           :  Integer,String
'''

emp = []

n = int(input('\n How Many Employees ? '))
print("\n")

for i in range(n):
    print('\n Enter Id : ', end='')
    emp.append(int(input()))
    
    print('Enter Name : ', end='')
    emp.append(input())
    
    print('Enter Salary : ', end='')
    emp.append(float(input()))
    
print('\n The List Is Created With Employee Data. ')

id = int(input('\n Enter Employee Id : '))
print("\n")

# Display Employee Details Upon Taking Id.

for i in range(len(emp)):
    if id == emp[i]:
        print('Id = {:d}, Name = {:s}, Salary = {:.2f}'.format(emp[i], emp[i+1], emp[i+2])) 
        break   
      