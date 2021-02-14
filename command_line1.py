'''
Description      :  Use Of Command Line Arguments 
Function Date    :  14 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''

import sys

def Addition(no1, no2):
    return no1 + no2

def main():
    ret = Addition(int(sys.argv[1]), int(sys.argv[2]))
    print("Addition is : ", ret)

if __name__ == "__main__":
    main()