# Python Program To Find The Length Of A String Without Using len() Function

'''
Function Name    :  Find Length Of String Using For-Loop. 
Function Date    :  3 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

str = input('Enter A String : ')
print("\n")


i = 0
for s in str:
    print(str[i], end= '')
    i += 1
     
print('\n\n Number Of Characters : ', i)