# Python Program To Randomly Access A Record From A Binary File

'''
Function Name    :  Randomly Access A Record From A Binary File
Function Date    :  25 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

# Record Length As 20 Characters

reclen = 20

# Open The File In Binary Modes For Reading

with open('cities.bin', 'rb') as f:
    n = int(input('Enter Records Numbers : '))
    
    # Move File Pointer To The End Of n-1 th Record
    
    f.seek(reclen * (n-1)) 
    
    # Get The n th Records With 20 Chars
    
    str = f.read(reclen)
    
    # Convert The Byte String Into Ordinary String
    
    print(str.decode())
    