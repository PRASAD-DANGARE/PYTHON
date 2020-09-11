# Python Program To Accept Elements In The Form Of A Tuple And Display Their Sum And Average

'''
Function Name    :   Accept Elements In Form Of Tuple And Display Sum, Average.
Function Date    :  11 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String,Integer
'''

num = eval(input("\n Enter Elements In () : "))
sum = 0
n = len(num) # n Is No Of Elements In The Tuple
for i in range(n): # Repeat i From 0 To n-1
    sum += num[i] # Add Each Elements To Sum
print('\n Sum Of Numbers : ', sum) # Display Sum
print('\n Average Of Numbers : ', sum/n) # Display Average
print("\n")