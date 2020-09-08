# Python Program To Find The Bigger Number In Two Given Number

'''
Function Name    :  Find Bigger Number In Two Given Number. 
Function Date    :  8 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer,Float
'''

max = lambda x, y: x if x > y else y # Write Lambda Function
a, b = [int(n) for n in input("Enter Two Numbers : ").split(',')]
print('Bigger Number = ', max(a, b) ) # Call Lambda Function