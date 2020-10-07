# Python Program To Download A Web Page From Internet And Save It Into Our Computer

'''
Function Name    :  Download WebPage From Internet And Save It Into Our Pc
Function Date    :  7 Oct 2020
Function Author  :  Prasad Dangare
Input            :  It Contain A HTML File
Output           :  Refer myfile.html For The Output
'''


import urllib.request

try:
    
    # Store The Url Of The Page Into File Object
    
    file = urllib.request.urlopen("https://www.python.org/")
    
    # Read Data From File And Store Into Content Object
    
    content = file.read()
    
except urllib.error.HTTPError:
    print('The Web Page Not Exist')
    exit()
    
# Open A File For Writing

f = open('myfile.html', 'wb')

# Write Content Into The File

f.write(content)

# Close The File

f.close()
