# Python Program To Know How  Function Can Return Another Function

'''
Function Name    :  One Function Return Another Function. 
Function Date    :  6 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String 
'''

def display():
    def message():
        return 'How Are U ? '
    return message

# Call Display() Function And It Returns Message() Function 
# In The Following Code, Fun Refers To The Name: Message.

fun = display()
print(fun()) 