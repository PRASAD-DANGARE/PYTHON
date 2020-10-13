# Python Program To Display Employee Id Numbers On X-Axis And Then Salaries On Y-Axis In The Form A Bar-Graph

'''
Function Name    :  Display Employee Id Numbers On X-Axis And Then Salaries On Y-Axis
Function Date    :  8 Oct 2020
Function Author  :  Prasad Dangare
Input            :  In This Program We Showing Bar-Graph Through Employee Salaries
Output           :  It Display Bar-Graph On Python3.8 Concole
'''

import matplotlib.pyplot as plt
import pandas as pd

# Take Employee Data As A Dictionary

empdata = {"empid": [1001, 1002, 1003, 1004, 1005, 1006],
           "ename": ["Prasad Dangare", "Hrutik Takke", "Shiva Das", "Shubham Lodha", "Sunder Pichai", "Ruth Porat"],
           "sal": [140000.20, 150000.10, 120000.40, 170000.05, 110000.12, 110000.80],
           "doj": [10-10-2000, 3-20-2002, 3-3-2000, 9-10-2000, 10-8-2000, 9-9-1999]}

# Create A Data Frame

df = pd.DataFrame(empdata)

# Extract empid And Salary Data Into X And Y Vars

x = df['empid']
y = df['sal']

# Create Bar Graph

plt.bar(x, y, label='Employee Data', color='red')

# Set X And Y Axis Labels

plt.xlabel('Employee Ids')
plt.ylabel('Employee Salaries')

# Set Company Title

plt.title('GOOGLE CO-SEATTLE, KIRKLAND')

# Show Legend

plt.legend()

# Display The Graph

plt.show()
