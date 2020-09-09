# Python Program That Returns Characters From A To C

'''
Function Name    :  Returns Characters From A To C.
Function Date    :  9 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
    
# Call Generator Function And Get Generator Object g

g = mygen()

# Display All Characters In The Generator

print(next(g)) # Dsiplay 'A'
print(next(g)) # Display 'B'
print(next(g)) # Display 'C'
print(next(g)) # Error

