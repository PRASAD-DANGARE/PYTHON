# Python Program To Understand How A Function Returns Two Values

'''
Function Name    :  One Function Returns Two Values . 
Function Date    :  2 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  Integer 
'''

def sum_sub(a, b):
    """This Function Returns Results Of 
       Addition And Subtraction Of a, b """
    
    c = a + b
    d = a - b
    return c, d

# Get The Result From The sum_sub() Function

x, y = sum_sub(10, 5)

# Display The Results

print("\n Result Of Addition : ", x)
print("Result Of Subtraction : ", y)
print("\n")

