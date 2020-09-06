# Python Program That Returns The Results Of Addition, Subtraction, Multiplication And Division

'''
Function Name    :  Returns The Results Of Add,Subtract,Multiply,Divide. 
Function Date    :  6 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer,Float 
'''

def sum_sub_mul_div(a, b):
    """ This Functions Returns Results Of Addition ,
        Subtraction , Multipication And Division Of a, b"""
        
    c = a + b
    d = a - b
    e = a * b
    f = a / b
    
    return c, d, e, f
        
# Get Results From sum_sub_mul_div_() Function And Store Into t

t = sum_sub_mul_div(10, 5)

# Display The Results Using For Loop

print('\n The Results Are : ')
for i in t:
    print(i, end= ', ')
    