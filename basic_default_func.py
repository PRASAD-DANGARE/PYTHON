'''
Description      :  Use Of Default Argument Values In Function 
Function Date    :  05 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''

def say(message, times = 1):
    print (message * times)

say('Hello')
say('Guys ', 5)