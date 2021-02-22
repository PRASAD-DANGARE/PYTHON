'''
Description      :  getrecursionlimit & setrecursionlimit
Function Date    :  22 Feb 2021
Function Author  :  Prasad Dangare
Input            :  ---
Output           :  ---

'''

import sys

def main():
    print("Recursion limit is : ", sys.getrecursionlimit())
    # due to stack frame memory is limited but in case of for and while loop it is dont showing

    sys.setrecursionlimit(1500)
    print("New Recursion limit is : ", sys.getrecursionlimit()) # It Just Display The Size But Actually It Is Not Allocated

if __name__ == "__main__":
    main()