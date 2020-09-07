# Python Program To Know How To Pass A Function As Parameters To Another Function

'''
Function Name    :  Pass A Function As Parameter To Another Function. 
Function Date    :  7 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String 
'''

def display(fun):
    return 'Hai ' + fun

def message():
    return 'Prasad How Are U ? '

# Call display() Function And Pass Message() Function

print(display(message()))