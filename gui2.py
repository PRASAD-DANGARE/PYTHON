'''
Function Name    :  Know The Available Font Families
Function Date    :  16 Oct 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String

'''

# Python Program To Know The Available Font Families

from tkinter import*
from tkinter import font

# Create Root Window

root = Tk()

# Get All The Supported Font Families

list_fonts = list(font.families())

# Display Them

print(list_fonts)
