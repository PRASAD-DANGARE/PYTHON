# Python Program To Create A Generator That Returns A Sequence Of Numbers From x To y

'''
Function Name    :  Create Generator That Returns Square Numbers From x To y. 
Function Date    :  9 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

def mygen(x, y):
    while x <= y:
        yield x
        x += 1
        
# Fill Generator Object With 5 And 10

g = mygen(5, 10)

# Display All Numbers In The Generator
 
for i in g:
    print(i, end = ' ')
        