# Python Program To Handle IO Error Produced By Open() Function

'''
Function Name    :  Open() Function
Function Date    :  23 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

try:
    name = input('Enter Filename : ')
    f = open(name, 'r')
    
except IOError:
    print('File Not Found : ', name)
    
else:
    n = len(f.readlines())
    print(name, 'has', n, 'lines')
    f.close()
    
    