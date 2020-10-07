# Python Program To Retrieve Different Parts Of The URL And Display Them

'''
Function Name    :  Retrieve Different Parts Of The URL And Display Them
Function Date    :  7 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import urllib.parse

# Take Any Url

url ='https://github.com/PRASAD-DANGARE'

# Get A Tuple With Parts Of The Url

tp1 = urllib.parse.urlparse(url)

# Display The Contents Of The Tuple

print(tp1)

# Display Different Parts Of The Url

print('scheme = ', tp1.scheme)
print('Net Location = ', tp1.netloc)
print('Path = ', tp1.path)
print('Parameters = ', tp1.params)
print('Port Number = ', tp1.port)
print('Total Url = ', tp1.geturl())

