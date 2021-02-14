'''
Description      :  Filter In Command Line Arguments 
Function Date    :  14 Feb 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int
'''

import sys

def Addition(no1, no2):
    return no1 + no2

def main():
    if (len(sys.argv) < 3) or (len(sys.argv) > 3):
        print("invalid number of arguments")
        return

    ret = Addition(int(sys.argv[1]), int(sys.argv[2]))
    print("Addition of {} and {} is {}.".format(sys.argv[1], sys.argv[2], ret))

if __name__ == "__main__":
    main()