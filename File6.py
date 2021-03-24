'''
Function Name    :  main()
Description      :  How To Open File & Read The Full Data 
Function Date    :  15 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

def main():

    name = input("Enter the file name : ")
    
    fobj = open(name,"r")
    
    print("Data from file is : ")
    
    for Data in fobj:
        print(Data,end="")
    
if __name__ == "__main__":
    main()