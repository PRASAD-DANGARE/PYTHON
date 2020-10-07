# Python Program To Create A TCP/IP Server Program That Sends Messages To A Client

'''
Function Name    :  Create A TCP/IP Server Program That Sends Messages To A Client
Function Date    :  7 Oct 2020
Function Author  :  Prasad Dangare
Input            :  In This Program There Are Some Message To Client1.py
Output           :  It Display In The Program Client1.py
'''

import socket

# Take The Server Name And Port Number

host = 'localhost'
port = 3000

# Create A Socket At Server Side Using TCP/IP Protocol

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind The Socket With Server And Port Number

s.bind((host, port))

# Allow Maximum 1 Connection To The Socket 

s.listen(1)

# Wait Till A Client Accepts Connection

c, addr = s.accept()

# Display Client Address

print("Connection From : ", str(addr))

# Send Messages To The Client After Encoding Into Binary String

c.send(b"Hello Client, How Are You")
msg = "Byee!"
c.send(msg.encode())

# Disconnect The Server

c.close()

 