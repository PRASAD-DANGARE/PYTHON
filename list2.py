# Python Program To Access List Elements Using Loops

'''
Function Name    :  Access List Elements Using Loops.
Function Date    :  10 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

list = [10,20,30,40,50]

print('Using While Loop')
i=0
while i<len(list): # Repeat From 0 To Length Of List 
    print(list[i])
    i=i+1
print('Using For Loop')
for i in list: # Repeat For All Elements
    print(i)