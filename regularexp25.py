# Python Program To Retrieve Information From A HTML File Using A Regular Expression


'''
Function Name    :  Regular Expression Retrieve Information From A HTML File
Function Date    :  29 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import re
import urllib.request

# Open The HTML File Using urlopen() Method

f = urllib.request.urlopen(r'file:///E:\python\breakfast.html')

# Read Data From The File Object Into Text String

text = f.read()

# Convert The Byte String Into Normal String

str = text.decode()

# Apply Regular Expression On The String

result = re.findall(r'<td>\w+</td>\s<td>(\w+)</td>\s<td>(\d\d.\d\d)</td>', str)

# Display The Items Of The Result

print(result)

# Display The Items Of The Result

for item, price in result:
    print('Item= %-15s Price= %-10s' %(item, price))
    
# Close The File

f.close()
