# Python Program To Know How To Define A Function Inside Another Function

'''
Function Name    :  Defining A Function Inside Another Function. 
Function Date    :  6 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String 
'''

def display(str):
    def message():
        print("\n")
        return 'How Are You '
    
    result = message()+str
    return result

# Call Display() Function

print(display("Prasad"))
print("\n")
