# python program to find sum of even numbers .
'''
Function Name    :  Sum Of Even Numbers
Function Date    :  26 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''
maximum = int(input("Please Enter The Maximum Value:"))
total = 0

for number in range (1, maximum + 1):
  if(number %2 == 0):
    print("{0}".format(number))
    total = total + number
    
    print("The Sum Of Even Numbers From 1 To {0} = {1}".format(number, total))
    

 