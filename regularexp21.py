# Python Program To Create A Regular Expression To Retrieve Marks And Names From A Given String

'''
Function Name    :  Regular Expression To Retrieve Marks And Names
Function Date    :  29 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

import re;
str = 'Prasad got 75 marks, Hrutik got 55 marks, whereas Shubham got 98 marks'

marks = re.findall('\d{2}', str) # Extract Only Marks Having 2 Digits
print(marks)

# Extract Names Starting With A Capital Letters & Remaining Alphabtic Characters

names = re.findall('[A-Z][a-z]*', str) 
print(names)


