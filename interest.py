'''
Function Name    :  Find Simple Interest Of An Amount
Function Date    :  17 Oct 2020
Function Author  :  Prasad Dangare
Input            :  Float
Output           :  Float

'''

# Python Program To Find The Simple Interest Of A Given Amount Through User

A = float(input("\n Enter Amount : "))

D = float(input("Enter Duration Of Years : "))

I = float(input("Enter Rate Of Interest : "))

interest = (A * D * I)/100

print("Simple Interest Are : {}".format(interest))
print("\n")
