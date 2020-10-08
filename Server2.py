# Python Program To Create A UDP Server That Sends Messages To The Client

'''
Function Name    :  Create A UDP Server That Sends Messages To The Client
Function Date    :  7 Oct 2020
Function Author  :  Prasad Dangare
Input            :  In This Program There Are Some Message To Client2.py
Output           :  It Display The Output In Program Client2.py
'''

import socket
import time

# Take The Server Name And Port Number

host = 'localhost'
port = 5000

# Create A Socket At Server Side To Use UDP Protocol

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Let The Server Waits For 5 Seconds

time.sleep(4)

# Send Messages To The Client After Encoding Into Binary String

s.sendto(b"Hello Client, How Are u", (host, port))
msg = "Byee!"
s.sendto(msg.encode(), (host, port))

# Disconnect The Server

s.close()

