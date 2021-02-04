'''
Description      :  Use Of While Loop With Continue Statement  
Function Date    :  04 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Str
Output           :  Str
'''

while True:
    s = input('Enter A String : ')
    if s == 'quit':
        break
    
    if len(s) < 3:
        print ('Too Small')
        continue
    print ('Input Is Of Sufficient Length')
