# Python Program To Convert Numbers From Other System Into Decimal Number System
'''
Function Name    :   Convert Other System To Decimal Number System
Function Date    :   25 Aug 2020
Function Author  :   Prasad Dangare
Input            :   Character,Integer
Output           :   Integer
'''
str = input('Enter Hexadecimal Number:') # Accept input as String
n = int(str, 16) # base 16 for Hexadecimal
print('Hexadecimal to Decimal =', n)
print("\n")

str = input('Binary Number:')
n = int(str, 2) # base 2 for Binary 
print('Binary To Decimal =', n) 
print("\n")

str = input('Octal Number:')
n = int(str, 8) # base 8 for Octal
print('Octal To Decimal =', n)
print("\n")