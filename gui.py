'''
Function Name    :  Create Root Window With Some Options
Function Date    :  15 Oct 2020
Function Author  :  Prasad Dangare
Input            :  In This Program New Root Window Is Open
Output           :  It Display Root Window With image.ico In Top Of It
'''

# Python Program To Create Root Windows With Some Options

from tkinter import*

root = Tk()  # Create Top Level Window

root.title("My Window")  # Set Window Title

root.geometry("400x300")  # Set Windows Size

# Set Windows Icon

root.wm_iconbitmap('image.ico')

root.mainloop()  # Display Window And Wait For Any Events
