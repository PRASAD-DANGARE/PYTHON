# Python Program To Delete A Specific Records From The Binary File

'''
Function Name    :  Delete A Specific Records From The Binary File
Function Date    :  26 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import os

reclen = 20 # Record Length As 20 Characters

size = os.path.getsize('cities.bin') # Find Size Of File

n = int(size/reclen) # Find Number Of Records In The Files

f1 = open('cities.bin', 'rb') # Open cities.bin For Reading

f2 = open('file2.bin', 'wb') # Open file2.bin For Writing 

# Accept City Name From Keyboard

city = input('Enter City Name To Delete: ')

# Add Spaces So That It Will Have 20 Characters Length

ln = len(city)
city = city+(reclen-ln)*' '

# Convert City Name To Binary String

city = city.encode()

# Repeat For All The n Records

for i in range(n):
    
    str = f1.read(reclen) # Read One Record From f1 File
    if(str != city): # If It Is Not The City Name, Store Into f2 File
        f2.write(str)
        
print('Record Deleted...')

# Close The Files

f1.close()
f2.close()

# Delete The cities.bin File

os.remove("cities.bin")

# Rename file2.bin As cities.bin

os.rename("file2.bin", "cities.bin")


