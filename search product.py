def findProd():
    f=0
    while f<1:
        print("Would you like to search using product names(N) or by product ID(I)")
        n=input()
        if(n=='N' or n=='n'):
            print("Please enter item name:")
            i=input()
            for x in products:
                if (i==x[1]):
                    print(x)
                    print("Would you like to search for another item?")
                    d=input()
                    if(d=='Y' or d=='y'):
                        break
                    elif(d=='N' or d=='n'):
                        f=2
                        break
                    else:
                        print("invalid")
                        break
            else:
                print("Item not found")
        elif(n=='I' or n=='i'):
            print("Please enter item ID:")
            i=input()
            for x in products:
                if(i==x[0]):
                    print(x)
                    print("Would you like to search for another item?(Y or N)")
                    d=input()
                    if(d=='Y' or d=='y'):
                        break
                    elif(d=='N' or d=='n'):
                        f=2
                        break
                    else:
                        print("invalid")
                        break
            else:
                print("Item not found")
        else:
            print("Invalid! Going back to the search selection")
    
