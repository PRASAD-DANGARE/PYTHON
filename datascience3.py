# Python Program To Display A Histogram Showing The Number Of Employees In Specific Age Groups

'''
Function Name    :  Display A Histogram Showing The Number Of Employees In Specific Age Groups
Function Date    :  8 Oct 2020
Function Author  :  Prasad Dangare
Input            :  In This Program We Showing Bar-Graph Of Particular Age Groups By Its ID NO
Output           :  It Display Bar-Graph On Python3.8 Concole
'''

import matplotlib.pyplot as plt

# Take Individual Employee Ages And Range Of Ages

emp_ages = [22, 45, 30, 59, 58, 56, 57, 45, 43, 43, 50, 40, 34, 33, 25, 19]
bins = [0, 10, 20, 30, 40, 50, 60]

# Create Histogram Of Bar Type

plt.hist(emp_ages, bins, histtype='bar', rwidth=0.8, color='cyan')

# Set Labels

plt.xlabel('Employee Ages')
plt.ylabel('No Of Employees')
plt.title('MICROSOFT CORP')
plt.legend()

# Draw The Histogram

plt.show()
