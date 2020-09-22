# Python Program To Handle The ZeroDivisionError Exception

'''
Function Name    :  Exception Handling
Function Date    :  22 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String,Integer
Output           :  String
'''

try:
    f = open("myfile", "w")
    a, b = [int(x) for x in input("Enter Two Numbers : ").split()]
    
    c = a/b
    f.write("Writing %d Into myfile" %c)
    
except ZeroDivisionError:
    print('Division By Zero Happened')
    print('Please Do Not Enter 0 In Input')
    
finally:
    f.close()
    print('File Is Closed')