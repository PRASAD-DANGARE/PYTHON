# Python Program To Know The Types Of Characters Entered By The User.

'''
Function Name    :  Identify Types Of Character Entered By Users . 
Function Date    :  3 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Strings
Output           :  Strings
'''

str = input('Enter A Character : ')
print("\n")

ch = str[0] # Takes Only The 0th Characters Into ch

# Test ch

if ch.isalnum():
    print('It Is Alphabet Or Numeric Character')
    print("\n")
    
    if ch.isalpha():
        print('It Is An Alphabet')
        print("\n")
        
        if ch.isupper():
            print('It Is Capital Letter')
            print("\n")
            
        else:
            print('It Is LowerCase Letter')
            print("\n")
    else:
        print('It Is A Numeric Digit')
        print("\n")

elif ch.isspace():
        print('It Is A Space')
        print("\n")

else:
    print('It May Be A Special Character')
    print("\n")
