'''
Description      :  Use Of Lambda Function  
Function Date    :  20 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Anonymous Functions
Output           :  --
'''

print("Demonstration of Lambda : Anonymous Functions")

# Defining Regular Function

def add(no1,no2):
    return no1 + no2

value1 = 10
value2 = 5
ret = add(value1,value2)

print("Addition is {} with regular function".format(ret))

# Defining Lambda Function ie Anonymous Functions

fp = lambda no1,no2 : no1 + no2
ret = fp(value1,value2)

print("Addition is {} with lambda function".format(ret))