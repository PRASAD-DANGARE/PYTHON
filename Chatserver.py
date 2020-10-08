# Python Program To Create A Basic Chat Server Program In Python

'''
Function Name    :  Create A Basic Chat Server Program In Python
Function Date    :  8 Oct 2020
Function Author  :  Prasad Dangare
Input            :  In This Program We Are Sending Messages To Chatclient.py
Output           :  It Display Messages In Chatclient.py
'''

import socket
host = '127.0.0.1'
port = 9000

# Create Server Side Socket

s = socket.socket()
s.bind((host, port))

# Let Maximum Number Of Connection Are 1 Only

s.listen(1)

# Wait Till A Client Connects

c, addr = s.accept()
print("A Client Connected")

# Server Runs Continuously

while True:
    
    # Receive Data Form Client
    
    data = c.recv(1024)
    
    # If Client Sends Empty String, Come Out
    
    if not data:
        break
    print("From Client : "+ str(data.decode()))
    
    # Enter Response Data From Server
    
    data1 = input("Enter Response : ")
    
    # Send That Data To Client
    
    c.send(data1.encode())
    
# Close Connection

c.close()

