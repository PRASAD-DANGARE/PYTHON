#  Python Program To Handle Syntax Error Given By eval() Function
'''
Function Name    :  eval() Function
Function Date    :  23 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

try:
    date = eval(input("Enter Date : "))
    
except SyntaxError:
    print("Invalid Date Entered")
    
else:
    print("You Entered : ", date)
    