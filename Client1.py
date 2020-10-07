# Python Program To Create TCP/IP Client Program That Receives Messages From The Server

'''
Function Name    :  Create A TCP/IP Client Program That Receives Messages From Server
Function Date    :  7 Oct 2020
Function Author  :  Prasad Dangare
Input            :  In This Program We Are Receiving  Message From Server1.py
Output           :  It Display In The Message Written By The Server1.py
'''

import socket

# Take The Server Name And Port Number

host = 'localhost'
port = 3000

# Create  Client Side Socket Using TCP/IP Protocol

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect It To Server And Port Number

s.connect((host, port))

# Receive Message String From Server, At A Time 1024 B

msg = s.recv(3072)

# Repeat As Long As Message Strings Are Not Empty

while msg:
    print('Received : '+msg.decode())
    msg = s.recv(3072)
    
# Disconnect The Client

s.close()

