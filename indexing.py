# Python Program To Access Each Elements Of A String In Forward And Reverse Order Using While-Loop

'''
Function Name    :  Access Each Elements Of String In Fordward And Reverse Order. 
Function Date    :  1 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

str = 'Core Python'

# Access Each Character Using While-Loop

n = len(str) # n = Number Of Chars In str
i = 0 # i = 0,1,2,3....n-1
while i < n:
    print(str[i], end= ' ')
    i += 1
    
print() # Put Cursor Into Next Line
    
# Access In Reverse Order

i =- 1 # i = -1,-2,-3....-n
while i >= -n:
    print(str[i], end= ' ')
    i -= 1
print() # Put Cursor Into Next Line

# Access In Reverse Into Next Line

i = 1 # 1,2,3....n
n = len(str) # n = Number Of Chars In str
while i <= n:
    print(str[-i], end= ' ')
    i += 1
  