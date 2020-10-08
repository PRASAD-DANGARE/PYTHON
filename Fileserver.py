# Python Program To Create A File Server That Receives A File Name From A Client 
# And Sends The Contents Of The File

'''
Function Name    :  File Server That Receive File Name And Its Content From Client
Function Date    :  8 Oct 2020
Function Author  :  Prasad Dangare
Input            :  In This Program We Are Receiving  File Name And Content From Fileclient.py
Output           :  It Display Same Content In Client Side In Fileclient.py
'''

import socket

# Take Server Name And Port Number

host = 'localhost'
port = 6767

# Create A TCP Socket

s = socket.socket()

# Bind Socket To Host And Port Number

s.bind((host, port))

# Maximum 1 Connections Is Accepted

s.listen(1)

# Waits Till Client Accepts A Connection

c, addr = s.accept()
print('A Client Accepted Connection')

# Accepts File From Client

fname = c.recv(1024)

# Convert File Name Into A Normal String

fname = str(fname.decode())
print("File Name Received From Client : "+fname)
try:
    
    # Open The File At Server Side
    
    f = open(fname, 'rb')
    
    # Read Content Of File 
    
    content = f.read()
    
    # Send File Content To Client
    
    c.send(content)
    print('File Content Sent To Client')
    
    # Close The File

    f.close()

except FileNotFoundError:
    c.send(b'File Does Not Exist')
    
# Disconnect Server

c.close()

    