'''
Function Name    :  main()
Description      :  How To Create File Using Open, w
Function Date    :  15 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''


def main():
    name = input("Enter the file name that you want to create : ")

    fobj = open(name, "w") # create new file

if __name__ == "__main__":
    main()