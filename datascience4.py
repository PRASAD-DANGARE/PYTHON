# Python Program To Display A Pie Chart Showing The Percentage Of Employees In Each Department Of A Company

'''
Function Name    :  Display A Pie Chart Of Google Depts In Percentage
Function Date    :  13 Oct 2020
Function Author  :  Prasad Dangare
Input            :  In This Program We Showing Pie Chart Of 4 Depts Of Google
Output           :  It Display Pie Chart In Percentage On Python3.8 Concole
'''


import matplotlib.pyplot as plt

# Take The Percentages Of Employee Of 4 Departments

slices = [50, 20, 15, 15]

# Take The Department Names

depts = ['AI', 'CLOUD', 'DataBase', 'ProductMgt']

# Take The Colors For Each Department

cols = ['magenta', 'cyan', 'red', 'gold']

# Create A Pie Chart

plt.pie(slices, labels=depts, colors=cols, startangle=90,
        explode=(0, 0.2, 0, 0), shadow=True, autopct='%.1f%%')

# Set Title And Legend

plt.title('GOOGLE CO-SEATTLE KIRKLAND')
plt.legend()

# Show The Pie Chart

plt.show()
