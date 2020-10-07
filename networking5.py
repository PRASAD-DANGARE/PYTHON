# Python Program To Download An Image From The Internet Into Our Computer System

'''
Function Name    :  Download An Image From The Internet Into Our Computer
Function Date    :  7 Oct 2020
Function Author  :  Prasad Dangare
Input            :  I Download The Google Kirkland Seattle Image In It
Output           :  Display The Image In Your Current Directory
'''

import urllib.request

# Copy The Image Address As Url

url = "https://livability.com/sites/default/files/Kirkland-Google.jpg" 

# Download The Image As myimage.jpg In Current Directory

download = urllib.request.urlretrieve(url, "myimage.jpg")
  