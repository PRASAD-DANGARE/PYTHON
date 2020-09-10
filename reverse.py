# Python Program To Display The Elements Of A List In Reverse Order

'''
Function Name    :  Display The Elements Of List In Reverse Order.
Function Date    :  10 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']

print('\n In Reverse Order 1 : ')
i = len(days) -1 # i Will Be 4
while i >= 0:
    print(days[i]) # Display From 4th To 0th Elements
    i -= 1
    
print('\n In Reverse Order 2 : ')
i =- 1 # Days[-1] Represents Last Elements
while i >=- len(days): # Display From -1th To -5th Elements
    print(days[i])
    i -= 1 