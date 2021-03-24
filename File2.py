'''
Function Name    :  main()
Description      :  How To Open File & Write The Data Using Open, Write
Function Date    :  15 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''


def main():
    
    name = input("Enter the file name that you want to Write : ")

    fobj = open(name, "w") # create new file

    str = input("Enter The Data That You Want To Write In The File : ")

    fobj.write(str)
    
if __name__ == "__main__":
    main()