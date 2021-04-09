'''
Function Name    :  main()
Description      :  Demonstration of dictionary  
Function Date    :  21 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

def main():
    
    batches = {"PPA":12500, "LB":11000, "Python": 13000, "Angular":10000}

    print(type(batches))
    print(len(batches))

    print(batches)

    print(batches["PPA"]) 

if __name__ == "__main__":
    main()