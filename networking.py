# Python Program To Find The IP Address Of A Website

'''
Function Name    :  Find The IP Address Of A Website
Function Date    :  7 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import socket
from socket import gaierror

# Take The Server Name

host = 'www.google.co.in'

try:
    
    # Know The IP Address Of The Website
    
    addr = socket.gethostbyname(host)
    print('IP Address = '+ addr)
    
except socket/gaierror: # If Get Address Info Error Occurs
    print('The Website Does Not Exist')
    