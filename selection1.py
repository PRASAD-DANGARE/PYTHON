'''
Description      :  Find Whether The Given Number Is Odd, Even 
Function Date    :  15 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Call The Function From selection.py

'''

'''def CheckEven(No):
    if No % 2 == 0:
        return True
    else:
        return False
'''

import selection as MN

def main():
    print("Enter One Number")
    value = int(input())

    bret = MN.CheckEven(value) # create boolean

    if bret == True:
        print("{} is Even number".format(value))
    else:
        print("{} is Odd number".format(value))

if __name__ == "__main__":
    main()   

