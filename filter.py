# Python Program Using filter() To Filter Out Even Numbers From A List

'''
Function Name    :  Use Of Filter() To Filter Even Numbers. 
Function Date    :  8 Sep 2020
Function Author  :  Prasad Dangare
Input            :  Integer
Output           :  Integer
'''

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
# Let Us Take A List Of Numbers

lst = [10,23,45,46,70,99]

# Call Filter() With is_even() And lst

lst1 = list(filter(is_even, lst))
print(lst1)