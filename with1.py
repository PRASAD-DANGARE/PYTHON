# Python Program To Use With To Open A File And Write Some Strings Into The File

'''
Function Name    :  Open A File And Write Some Strings Into The File
Function Date    :  24 Sep 2020
Function Author  :  Prasad Dangare
Input            :  String
Output           :  String
'''

with open('sample.txt', 'w') as f:
    f.write('\n I Am Prasad Dangare')
    f.write('Python Is The Attraction ')
    