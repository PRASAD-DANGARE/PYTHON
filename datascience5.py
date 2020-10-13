# Python Program To Create A Line Graph To Show The Profile Of A Company In Various Years

'''
Function Name    :  Create A Line Graph To Show The Profile Of A Company
Function Date    :  13 Oct 2020
Function Author  :  Prasad Dangare
Input            :  In This Program We Showing Line Graph Of MICROSOFT INC
Output           :  It Display Line Graph On Python3.8 Concole
'''

import matplotlib.pyplot as plt

years = ['2012', '2013', '2014', '2015', '2016', '2017']
profits = [9, 10, 10.5, 8.8, 10.9, 9.75]

# Create The Line Graph

plt.plot(years, profits, 'blue')

# Set Title And Labels

plt.title('MICROSOFT INC')
plt.xlabel('YEARS')
plt.ylabel('PROFITS IN MILLIONS RS')

# Show The Line Chart

plt.show()
