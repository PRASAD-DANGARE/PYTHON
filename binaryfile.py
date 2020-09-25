# Python Program To Create A Binary File And Store A Few Records

'''
Function Name    :  Create A Binary File And Store A Few Records
Function Date    :  25 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

reclen = 20

# Open The File In wb Mode As Binary File

with open("cities.bin", "wb") as f:
    
    # Write Data Into The File
    
    n = int(input("How Many Entries ? "))
    
    for i in range(n):
        city = input('Enter City Names : ')
        
        # Find The Length Of City
        
        ln = len(city)
        
        # Increase The City Name To 20 Chars
        # By Adding Remaining Spaces
        
        city = city + (reclen-ln)*' '
        
        # Convert City Name Into Bytes String
        
        city = city.encode()
        
        # Write The City Name Into The File
        
        f.write(city)
        
        
        
    