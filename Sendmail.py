# Python Program To Create A Python Program To Send Email To Any Mail Address

'''
Function Name    :  Python Program To Send Email To Any Mail Address
Function Date    :  8 Oct 2020
Function Author  :  Prasad Dangare
Input            :  In This Program We Are Sending Messages To My Gmail Account
Output           :  It Display Messages In Gmail Account
'''

import smtplib
from email.mime.text import MIMEText

# First Type The Body Text For Our Mail

body = ''' This Is My Text Mail. This Is Send To You From My Python 
      Program. I Think You Appreciated Me.'''
      
# Create MIMEText Class Object With Body Text

msg = MIMEText(body)

# From Which Address The Mail Is Sent

fromaddr = "prasaddagare93@gmail.com"

# To Which Address The Mail Is Sent

toaddr = "sunitadangare14@gmail.com"

# Store The Address Into msg Object

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "HAI FRIEND"

# Connect To Gmail.com Server Using 587 Port Number

server = smtplib.SMTP('smtp.gmail.com', 587)

# Put The smtp Connection In TLS Mode

server.starttls()

# Login To The Server With Your Correct Password

server.login(fromaddr, "mypassword")

# Send The Message To The Server

server.send_message(msg)
print('Mail Sent...')

# Close Connection With Server

server.quit()
