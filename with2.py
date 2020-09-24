# Python Program To Use With To Open A File And Read Data From It

'''
Function Name    :  Open A File And Read Data From It
Function Date    :  24 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

with open('sample.txt', 'r') as f:
    for line in f:
        print(line)
        
    