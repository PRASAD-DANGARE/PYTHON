# Python Program That Reads The Source Code Of A Webpage

'''
Function Name    :  Reads The Source Code Of A Webpage
Function Date    :  7 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import urllib.request

# Store The Url Of The Page Into File Object

file = urllib.request.urlopen("https://www.python.org/")

# Read Data From File And Display

print(file.read())

