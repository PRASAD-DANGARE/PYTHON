# Python Program To Create A UDP Client That Receives Messages From The Server

'''
Function Name    :  Create A UDP Server That Receives Messages From Server
Function Date    :  7 Oct 2020
Function Author  :  Prasad Dangare
Input            :  In This Program We Are Receiving  Message From Server2.py
Output           :  It Display In The Message Written By The Server2.py
'''

import socket

# Take The Server Name And Port Number

host = 'localhost'
port = 5000

# Create A Client Side Socket That Uses UDP Protocol

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Connect It To Server With Host Name And Port Number

s.bind((host, port))

# Receive Message String From Server , At A Time 1024 B

msg, addr = s.recvfrom(3072)

try:
    
    # Let The Socket Blocks After 5 Seconds If The Server Disconnects
    
    s.settimeout(4)
    
    # Repeat As Long As Message Strings Are Not Empty
    
    while msg:
        print('Received : '+ msg.decode())
        msg, addr = s.recvfrom(3072)
        
except socket.timeout:
    print('Time Is Over And Hence Terminating...')
    
# Disconnect The Client

s.close()
  