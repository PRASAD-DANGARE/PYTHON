# Python Program That Create A Basic Chat Client Program In Python

'''
Function Name    :  Create A Basic Chat Client Program In Python
Function Date    :  8 Oct 2020
Function Author  :  Prasad Dangare
Input            :  In This Program We Are Sending Messages To Chatserver.py
Output           :  It Display Messages In Chatserver.py
'''

import socket
host = '127.0.0.1'
port = 9000

# Create Client Side Socket

s = socket.socket()
s.connect((host, port))

# Enter Data At Client

str = input("Enter Data : ")

# Continue As Long As Exit Not Entered By User

while str != 'exit':
    
    # Send Data From Client To Server
    
    s.send(str.encode())
    
    # Receive The Responce Data From Server
    
    data = s.recv(1024)
    data = data.decode()
    print("From Server : "+data)
    
    # Enter Data
    
    str = input("Enter Data : ")
    
# Close Connection

s.close()
