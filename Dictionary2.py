'''
Function Name    :  main()
Description      :  Variations On Dictionary  
Function Date    :  21 Mar 2021
Function Author  :  Prasad Dangare
Input            :  Int
Output           :  Int

'''

def main():
    
    batches = {"PPA":12500, "LB":11000, "Python": 13000, "Angular":10000}
    batches["LSP"] = 11000

    print("Key of dictionary : ")
    for value in batches.keys():
        print(value)

    print("Key and values of dictionary : ")
    for value in batches.keys():
        print(value, batches[value])

    print("Key and values are : ")
    for i, j in batches.items():
        print(i, j)

if __name__ == "__main__":
    main()