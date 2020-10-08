# Python Program To Create File Client Program That Sends A File Name To The Server 
# And Receives The File Contents

'''
Function Name    :  File Client That Send File Name And Its Content To Server
Function Date    :  8 Oct 2020
Function Author  :  Prasad Dangare
Input            :  In This Program We Are Sending File Name And Content To Fileserver.py
Output           :  It Display Same Content In Server Side In Fileserver.py
'''

import socket

# Take Server Name And Port Number

host = 'localhost'
port = 6767

# Create A TCP Socket

s = socket.socket()

# Connect To Server

s.connect((host, port))

# Type File Name From The Keyboard

filename = input("Enter Filename : ")

# Send The File Name To The Server 

s.send(filename.encode())

# Receive File Content From Server

content = s.recv(1024)
print(content.decode())

# Disconnect The Client

s.close()

