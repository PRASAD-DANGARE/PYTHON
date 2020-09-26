# Python Program To Create Phone Book With Names And Phone Numbers

'''
Function Name    :  Create Phone Book With Names And Phone Numbers 
Function Date    :  26 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

# Open The File In wb Mode As Binary File

from os import name


with open("phonebook.dat", "wb") as f:
    n = int(input('How Many Entries ? ')) # Write Data Into The File
    
    for i in range(n):
        name = input('Enter Name : ')
        phone = input('Enter Phone Number : ')
        
        # Convert Name And Phone From String To Bytes
        
        name = name.encode()
        phone = phone.encode()
        f.write(name+phone) # Write The Data Into The File
        