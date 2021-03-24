'''
Function Name    :  main()
Description      :  How To Open File & Read Single Line Of Data
Function Date    :  15 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

def main():

    name = input("Enter the file name : ")
    
    fobj = open(name,"r")
    
    print("single line from file is : ")
    print(fobj.readline())
    
if __name__ == "__main__":
    main()