'''
Function Name    :  main()
Description      :  How To Open File & Read Number Of Characters
Function Date    :  15 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

def main():

    name = input("Enter the file name that you want to Read : ")
    
    fobj = open(name,"r")   # create new file
    size = int(input("Enter number of characters to read : "))
    
    print("Data from file is ")
    print(fobj.read(size))
    
if __name__ == "__main__":
    main()