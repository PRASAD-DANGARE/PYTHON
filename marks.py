# Python Program To Storing Students Marks Into An Array And Finding Total Marks And Percentage Of Marks.

'''
Function Name    :  Storing Student Total Marks And Percentage Of Marks. 
Function Date    :  28 Aug 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Float
'''

from array import*

str = input('Enter Marks One By One : ').split(' ') # User Will Enter Marks As Per Her.
print("\n")
marks = [int(num) for num in str]
 
'''
Marks Is The Name Of Array. It Takes Each Number From str And Store It Into num.
The num Value Is Created Into Int(num) And Store Into Marks Array.
'''
  
sum = 0
for x in marks:
    print(x)
    sum += x
    print('Total Marks :', sum)
    
    '''
The Printing x Value That Presents Each Elements Each Elements Of Marks 
Array And Then Adding x Value To Sum.
'''

    n = len(marks) # Divide The Total Marks And Find Percent.
    percent = sum/n
    print('Percentage :', percent)
    print("\n")
    