# Python Program To Display Prime Numbers

'''
Function Name    :  Display Prime Number
Function Date    :  27 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

max = int(input("Up To Maximum Number? "))

for num in range(2, max + 1): # Generate From 2 Onwards Till max
  for i in range(2, num): # i Represents Number From 2 To num-1
   if (num % i) == 0: # If num Is Divisible By i
    break # Then It Is Not Prime Number, Hence Go Back And Check Next Number
  else:
   print(num) # Otherwise It Is Prime Number And Hence Display
          