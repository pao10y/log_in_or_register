def findProd():
    f=0
    while f<1:
        print("Would you like to search using product names(N) or by product ID(I)")
        n=input()
        if(n=='N' or n=='n'):
            print("Please enter item name:")
            i=input()
            y=0
            for x in products:
                y=y+1
                if (i==products[y][1]):
                    print(products[y])
                    print("Would you like to search for another item?")
                    d=input()
                    if(d=='Y' or d=='y'):
                        break
                    elif(d=='N' or d=='n'):
                        f=2
                    else:
                        print("invalid")
                        break
            else:
                print("Item not found")
        elif(n=='I' or n=='i'):
            print("Please enter item ID:")
            i=input()
            y=0
            for x in products:
                y=y+1
                if(i==products[y][0]):
                    print(products[y])
                    print("Would you like to search for another item?(Y or N)")
                    d=input()
                    if(d=='Y' or d=='y'):
                        break
                    elif(d=='N' or d=='n'):
                        f=2
                    else:
                        print("invalid")
                        break
            else:
                print("Item not found")
        else:
            print("Invalid! Going back to the search selection")
    
