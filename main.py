products=[["PRODUCT ID", "PRODUCT NAME","CATEGORY", "STOCKS", "PRICE"],
            ["S0001","WH-CH510 Wireless Headphone","Headphones",10,2999.00],
            ["S0002","MDR-XB55AP EXTRA BASS","Headphones",3,1499.00],
            ["S0003","XB550AP EXTRA BASS","Headphones",8,2999.00],
            ["S0004","W830 Compact Camera","Camera",10,6999.00],
            ["S0005","H300 Camera","Camera",7,12999.00],
            ["S0006","XB01 EXTRA BASS","Speaker",15,1999.00],
            ["S0007","GTK-PG10 Outdoor Speaker","Speaker",2,12999.00],
            ["S0008","XB32 EXTRA BASS","Speaker",12,6799.00],
            ["S0009","MDR-E9LP In-ear","Earphones",15,499.00],
            ["S0010","MDR-XB55AP In-ear","Earphones",9,1499.00],
            ["S0011","WI-SP51 Wireless In-ear","Earphones",6,4299.00],
            ["S0012","WS410 Walkman","MP3 Player",3,4999.00],
            ["S0013","A50 Walkman","MP3 Player",5,9999.00],
            ["S0014","WS620 Walkman","MP3 Player",5,6999.00],
            ["S0015","WF-XB700 Truly Wireless","Headphones",6,6799.00],
            ["S0016","XPeria XA","Cellphone",14,10690.00],
            ["S0017","XPeria X","Cellphone",10,15890.00],
            ["S0018","XPeria XA2 Ultra","Cellphone",10,24490.00],
            ["S0019","XPeria XA1","Cellphone",13,14890.00],
            ["S0020","XPeria XA1 Ultra","Cellphone",3,19090.00],]
idIncrement = [21]

# nested list of admin usernames and their passwords
admin_users = [
    ["admin_name", "1234"]
]

# nested list of registered usernames and their passwords
registered_users = [
    ["username", "1234"]
]

# LOG IN METHOD
def log_in():
    while True:
        print("\nLog-In")
        username = input("Enter username: ")
        password = input("Enter password: ")
        for i in registered_users:
            if username.lower() == i[0].lower():
                username = i[0]
        
        credentials = [username, password]
        
        if credentials in admin_users:
            print("Admin User: {}".format(username))
            return 1 
        elif credentials in registered_users:
            print("Registered User: {}".format(username))
            return 2 
        else:
            return
    
# REGISTER METHOD
def register(): # admin registers are closed, no outside user can be an admin
    print("\nRegister") 
    while True:
        r_username = input("Enter your username: ")
        for i in registered_users:
            if r_username.lower() == i[0].lower():
                print("Username Already Taken")
                return 3
        break
    r_password = input("Enter password: ")
    r_repassword = input("Re-enter password: ")
    if r_password == r_repassword:
        # more information details can be implemented if necessary

        r_credentials = [r_username, r_password]

        registered_users.append(r_credentials)
        print("Successfully registered! Now please log in :)")
        return 3
    else:
        print("Re-entered password and password must be the same, returning to initial prompt")
        return 3
#SHOW PRODUCTS FUNCTION
def listProd():
    l = [0,0,0,0,0]
    for lists in products:
        for i in range(5):
            if l[i] < len(str(lists[i])):
                l[i] = len(str(lists[i]))
    print("\n__________________________________________________________________________________________\n")
    for item in products:
        for i in range(5):
            if i == 4 and not item[i] == products[0][4]:
                print("₱"+"{:,.2f}".format(item[i]), end="")
            else:
                print(item[i], end=(" "*((l[i]+5) - len(str(item[i])))) )
        print()
    print("\n__________________________________________________________________________________________\n")

# ADD PRODUCT
def Add_product():
    listProd()
    while True:
        try:
            n=input("Enter name of product: ")
            c=input("Enter category: ")
            s=int(input("Enter stocks: "))
            p=int(input("Enter price: "))
            print("Item: ",n)
            print("Category: ",c)
            print("Stock: ",s)
            print("Price: ",p)
            resp=input("do you want to add this item? [Y/N]:  ")
            if resp.lower() == "y":
                id = "S" + str(idIncrement[0]).zfill(4)
                idIncrement[0] += 1
                products.append([id,n,c,s,p])
                listProd()
                print("addition success")
            elif resp.lower() == "n":
                print("addition cancelled")
            else:
                print("invalid input")
            resp=input("do you want to add another item? [Y/N]:  ")
            if resp.lower() == "y":
                continue
            elif resp.lower() == "n":
                break
            else:
                print("invalid input, defaulting to N")
                break
        except:
            print("Something went wrong, please try again")
            continue

#DELETE FUNCTION
def delete_product():
    verify = 0
    resp = "y"

    listProd()  # print list function

    while True:
        prodDel = input("\n\tEnter Product ID: ")
        for item in products:
            if prodDel.lower() == item[0].lower():
                products.remove(item)
                verify = 1
        if verify == 1:
            listProd()  # print list function
            print("\t\tProduct deleted...")
            verify = 0
        else:
            print("\t\tProduct not found...")

        resp = input("\n\tDelete another product [Y/N]: ")
        if resp.lower() == "y":
            continue
        elif resp.lower() == "n":
            break
        else:
            print("\tInvalid choice, defaulting to N")
            break
            
#UPDATE FUNCTION
def update_product():
    verify = 0
    resp = "y"

    listProd()  # print list function

    while True:
        loc = input("Enter Product ID: ")
        for i in products:
            if i[0].lower() == loc.lower():
                print("Updating Product: ", i)
                i[1] = input("Enter Product Name: ")
                i[2] = input("Enter Category: ")         
                i[3] = int(input("Enter Stocks: "))
                i[4] = int(input("Enter Price: "))
                verify = 1
                break
        if verify == 1:
            listProd()  # print list function
            print("\t\tProduct Updated...")
            verify = 0
        else:
            print("\t\tProduct Not Found...")

        resp = input("\n\tUpdate Another Product [Y/N]: ")
        if resp.lower() == "y":
            continue
        elif resp.lower() == "n":
            break
        else:
            print("\tInvalid Choice, Defaulting to N")
            break

#SEARCH FUNCTION
def findProd():
    f=0
    while f<1:
        print("Would you like to search using product names(N) or by product ID(I)")
        n=input()
        if(n=='N' or n=='n'):
            print("Please enter item name:")
            i=input()
            verify = 0
            for x in products:
                if (i.lower() in x[1].lower()):
                    print(x)
                    verify = 1
            if verify == 1:
                print("Would you like to search for another item?[Y/N]")
                d=input()
                if(d=='Y' or d=='y'):
                    continue
                elif(d=='N' or d=='n'):
                    break
                else:
                    print("Invalid, Default to N")
                    break
            else:
                print("Item not found")
        
        elif(n=='I' or n=='i'):
            print("Please enter item ID:")
            i=input()
            for x in products:
                if(i.lower()==x[0].lower()):
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
            
# MAIN FUNCTION
def main():
    while True:
        print("Sales Inventory System")

        user_input = input("(1) Log-In or (2) Register, (3) to exit (Enter #): ")

        if user_input.isdigit():
            if int(user_input) == 1:
                admin_or_user = log_in()
            elif int(user_input) == 2:
                admin_or_user = register()
            elif int(user_input) == 3:
                print("Program Terminated\n")
                break
            else:
                print("Invalid input. Please try again :(\n")
                continue
        else:
            print("Invalid input. Please try again :(\n")
            continue
        if admin_or_user == 1:
            while True:
                print("1. Add new product")
                print("2. Delete product")
                print("3. View all products")
                print("4. Update a product")
                print("5. Search product")
                print("6. Sales History")
                print("7. Log-out")
                choice = input()
                if choice == '1':
                    Add_product()
                elif choice == '2':
                    delete_product()
                elif choice == '3':
                    listProd()
                elif choice == '4':
                    update_product()
                elif choice == '5':
                    findProd()
                elif choice == '6':
                    print("This function is currently unavailable.")
                elif choice == '7':                    
                    print("Logging out...")
                    break
                else:
                    print("invalid choice.\n")
        elif admin_or_user == 2:
            print("Access to all registered user functions")
        elif admin_or_user == 3:
            continue
        else:
            print("User not Found :(\n")

main() # calls the main function for the code to run
