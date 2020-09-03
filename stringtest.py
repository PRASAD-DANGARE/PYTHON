# Python Program To Use The String Testing Methods  

'''
Function Name    :  String Testing Methods . 
Function Date    :  3 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer,String
Output           :  Integer,String
'''

# Check If All The Characters In The Text Are Alphanumeric Using isalnum() Method

txt = "Company12"

x = txt.isalnum()

print(x)
print("Next \n")

# Check If All The Characters In The Text Are Letters Using isalpha() Method

txt = "CompanyX"

x = txt.isalpha()

print(x)
print("Next \n")

# Check If All The Characters In The Text Are Digits Using isdigit() Method

txt = "50800"

x = txt.isdigit()

print(x)
print("Next \n")

# Check If All The Characters In The Text Are In Lower Case Using islower() Method

txt = "hello world!"

x = txt.islower()

print(x)
print("Next \n")

# Check If All The Characters In The Text Are In Upper Case Using isupper() Method

txt = "THIS IS NOW!"

x = txt.isupper()

print(x)
print("Next \n")

# Check If Each Word Start With An Upper Case Letter Using istitle() Method

txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)
print("Next \n")

# Check If All The Characters In The Text Are Whitespaces Using isspace() Method

txt = "   "

x = txt.isspace()

print(x)
print("Last \n")