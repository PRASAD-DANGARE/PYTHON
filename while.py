'''
Description      :  Use Of while With if, elif, else Statement
Function Date    :  04 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''

num = 23
running = True

while running :
 
    num = int(input ('Enter An Integer : '))
    
    if num == 23 :
        print ('Congratulations, You Guessed It.')
        running = False # this causes the while loop to stop
    
    elif num != 23 :
        print ('No, It Is A Little Higher Than That.')
    
    else:
        print ('No, It Is A Little Lower Than That.')
    
else :
    print ('The While Loop Is Over.')
    
print ('Done')