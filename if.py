'''
Description      :  Use Of if-Statement  
Function Date    :  04 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''

num = 23

num = int(input("Enter An Integer : "))

if num == 23:

    print ('Congratulations, you guessed it.')
    print ('but you do not win any prizes!')

elif num != 23:
 
    print ('No, it is a little higher than that')

else:
    
    print ('No, it is a little lower than that')
    print ('Done')