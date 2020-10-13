# Python Program To Display Employee Id Number On X-Axis And Their Salaries On Y-Axis In The Form Of Bar-Graph
# For Two Departments Of Company

'''
Function Name    :  Display Employee Id Numbers On X-Axis And Then Salaries On Y-Axis
Function Date    :  8 Oct 2020
Function Author  :  Prasad Dangare
Input            :  In This Program We Showing Bar-Graph Of 2 Dept As Sales , Production
Output           :  It Display Bar-Graph On Python3.8 Concole
'''

import matplotlib.pyplot as plt

# Take Employee Ids And Salaries For Sales Dept

x = [1001, 1003, 1006, 1007, 1009, 1011]
y = [10000, 23000.50, 18000.33, 16500.50, 12000.75, 9999.99]

# Take Employee Ids And Salaries For Production Dept

x1 = [1002, 1004, 1010, 1008, 1014, 1015]
y1 = [5000, 6000, 4500.00, 12000, 9000, 10000]

# Create Bar-Graph

plt.bar(x, y, label='Sales Dept', color='red')
plt.bar(x1, y1, label='Production Dept', color='green')

# Set The Labels And Legend

plt.xlabel('Emp Id')
plt.ylabel('Salaries')
plt.title('GOOGLE CO-SEATTLE KIRKLAND')
plt.legend()

# Display The Bar Graph

plt.show()
