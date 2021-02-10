import copy
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
idIncrement = [21,1]

sales = copy.deepcopy(products)
for i in sales:
    if i[3] == "STOCKS":
        i[3] = "SALES"
    else:
        i[3] = 0
# nested list of admin usernames and their passwords
admin_users = [
    ["admin_name", "1234"],
    ["iStunniq","admin"]
]

# nested list of registered usernames and their passwords
registered_users = [
    ["username", "1234",[],[],0]
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
        for i in admin_users:
            if username.lower() == i[0].lower():
                username = i[0]        
        credentials = [username, password]
        
        if credentials in admin_users:
            print("Admin User: {}".format(username))
            return 1 
        else:
            valid = 0
            for i in registered_users:
                if i[0] == username:
                    if i[1] == password:
                        print("Registered User: {}".format(username))
                        return i
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
        for i in admin_users:
            if r_username.lower() == i[0].lower():
                print("Username Already Taken")
                return 3
        break
    r_password = input("Enter password: ")
    r_repassword = input("Re-enter password: ")
    if r_password == r_repassword:
        # more information details can be implemented if necessary

        r_credentials = [r_username, r_password,[],[],0]

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
#SHOW SALES FUNCTION
def listSales():
    l = [0,0,0,0,0]
    for lists in sales:
        for i in range(5):
            if l[i] < len(str(lists[i])):
                l[i] = len(str(lists[i]))
    print("\n__________________________________________________________________________________________\n")
    total = 0
    for item in sales:
        if not item == sales[0]:
            total = total + (item[3]*item[4])
        for i in range(5):
            if i == 4 and not item[i] == sales[0][4]:
                print("₱"+"{:,.2f}".format(item[i]), end="")
            else:
                print(item[i], end=(" "*((l[i]+5) - len(str(item[i])))) )
        print()
    print("\nTotal value of sales: ₱{:,.2f}".format(total))
    print("__________________________________________________________________________________________\n")

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
                sales.append([id,n,c,0,p])
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
        if len(products) == 1:
            print("No products to delete")
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
        try:
            loc = input("Enter Product ID: ")
            print("1. Full Edit")
            print("2. Edit Name")
            print("3. Edit Category")
            print("4. Edit Stock")
            print("5. Edit Price")
            choice = input()
            if choice == "1":
                for i in products:
                    if i[0].lower() == loc.lower():
                        print("Updating Product: ", i)
                        a = input("Enter Product Name: ")
                        b = input("Enter Category: ")         
                        c = int(input("Enter Stocks: "))
                        d = int(input("Enter Price: "))
                        i[1] = a
                        i[2] = b
                        i[3] = c
                        i[4] = d
                        verify = 1
                        break
                for i in sales:
                    if i[0].lower() == loc.lower():
                        i[1] = a
                        i[2] = b
                        i[4] = d
                        verify = 1
                        break
            elif choice == "2":
                for i in products:
                    if i[0].lower() == loc.lower():
                        print("Updating Product: ", i)
                        x = i[0]
                        a = input("Enter Product Name: ")
                        i[1] = a
                        verify = 1
                        break
                for i in sales:
                    if i[0].lower() == loc.lower():
                        i[1] = a
                        break
            elif choice == "3":
                for i in products:
                    if i[0].lower() == loc.lower():
                        print("Updating Product: ", i)
                        x = i[0]
                        b = input("Enter Category: ")         
                        i[2] = b
                        verify = 1
                        break
                for i in sales:
                    if i[0].lower() == loc.lower():
                        i[2] = b
                        break
            elif choice == "4":
                for i in products:
                    if i[0].lower() == loc.lower():
                        print("Updating Product: ", i)
                        x = i[0]        
                        c = int(input("Enter Stocks: "))
                        i[3] = c
                        verify = 1
                        break
            elif choice == "5":
                for i in products:
                    if i[0].lower() == loc.lower():
                        print("Updating Product: ", i)
                        x = i[0]    
                        d = int(input("Enter Price: "))
                        i[4] = d
                        verify = 1
                        break
                for i in sales:
                    if i[0].lower() == loc.lower():
                        i[4] = d
                        break
            else:
                int("i")
            if verify == 1:
                listProd()  # print list function
                print("\t\tProduct Updated...")
                verify = 0
            else:
                print("\t\tProduct Not Found...")
        except:
            print("something went wrong, invalid input")
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
        print("Please enter item name:")
        name=input()
        verify = 0
        l = [0,0,0,0,0]
        for lists in products:
            for i in range(5):
                if l[i] < len(str(lists[i])):
                    l[i] = len(str(lists[i]))
        for item in products:
            if item == products[0] or name.lower() in item[1].lower():                
                for i in range(5):
                    if i == 4 and not item[i] == products[0][4]:
                        print("₱"+"{:,.2f}".format(item[i]), end="")
                    else:
                        print(item[i], end=(" "*((l[i]+5) - len(str(item[i])))) )
                print()
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
            print("No item found with {}".format(name))
            
#SALES HISTORY
def sales_history():
    total_sales=0
    print ("\nSales History \n")
    for idx, item in enumerate(bought):        
        print("\tItem {}: \n\t\tItem Name: {} \n\t\tProductID: {} \n\t\tCategory: {} \n\t\tQuantity: {} \n\t\tUnit Price: ₱{:,.2f} \n\t\tTotal Price: ₱{:,.2f}  ".format(idx + 1, item[0], item[3], item[4], item[1], item[2],item[2] * item[1]))
        total_sales= total_sales+(item[1]*item[2])
    print ("\n\tTOTAL SALES: ",total_sales)
    return

# ---------------------------------------USER FUNCTIONS--------------------------------------------
#Add to cart Function
def add_to_cart(user):
    print("\nAdd To Cart") 
    while True:
        input_item = input("Please Enter a Valid Product ID: ")
        for idx, item in enumerate(products):
            if input_item.upper() == products[idx][0]:
                input_itemno = int(input("How many product do you want to add to cart: "))
                if input_itemno <= products[idx][3]:
                    products[idx][3] = products[idx][3] - input_itemno
                    newcart = [products[idx][0],products[idx][1],input_itemno]
                    user[2].append(newcart)
                    print("{} {} successfully added to cart! :)\n".format(input_itemno, products[idx][2]))
                    return
        print("Invalid input. Please try again :(\n")
        return
def view_cart(user):
    print("\nView Cart")
    total = 0
    print("You have {} item/s in the cart: ".format(len(user[2])))
    for idx, item in enumerate(user[2]):
        print("\tItem {}: {} {}".format(idx + 1, item[2], item[1]))
        for i in products:
            if item[0] == i[0]:
                total = total + (int(item[2])*i[4])
    print("Total Cost: ₱{:,.2f}".format(total))
    return total
def delete_cart(user):
    verify = 0

    while True:
        if len(user[2]) == 0:
            print("Cart is Empty")
            break
        view_cart(user)  # print list function
        itemdel = int(input("\n\tEnter Item Number: "))
        for idx, item in enumerate(user[2]):
            for i in products:
                if item[0] == i[0]:
                    i[3] = i[3] + item[2]
        del user[2][itemdel-1]
        print("Item Deleted")
        view_cart(user)

        p = input("\n\tDelete another product [Y/N]: ")
        if p.lower() == "y":
            continue
        elif p.lower() == "n":
            break
        else:
            print("\tInvalid choice, defaulting to N")
            break

def checkOut(user):

    print("\n\nCHECK OUT______________________________________")
    if len(user[2]) == 0:
        print("Cart is Empty")
        return
    total = view_cart(user)
    print("Balance: ₱{:,.2f}".format(user[4]))
    print("Do you want to Check-Out?[Y/N]")
    choice = input().lower()
    if choice =="n":
        return
    if total <= user[4]:
        for idx, item in enumerate(user[2]):
            user[3].append(item)
            for i in sales:
                if item[0] == i[0]:
                    i[3] += item[2]
        receipt = "#"+str(idIncrement[1]).zfill(6)
        user[3].append(receipt)
        idIncrement[1] += 1
        user[2].clear()
        user[4] -= total
        print("Products successfully purchased, please check your orders to verify. your receipt is {}".format(receipt))
        return
    else:
        print("Insufficient cash!")

def view_orders(user):
    print("\nView Orders")
    incr = 1
    if len(user[3]) == 0:
        print("You have no orders to display")
    for idx, item in enumerate(user[3]):
        if type(item) == str:
            print("Receipt for above items: {}".format(item))
            incr = 1
        else:
            print("\tItem {}: {} {}".format(incr, item[2], item[1]))
            incr += 1
    return

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
                print("1. View all products")
                print("2. Add new product")
                print("3. Delete product")
                print("4. Update a product")
                print("5. Search product")
                print("6. Sales History")
                print("7. Log-out")
                choice = input()
                if choice == '1':
                    listProd()
                elif choice == '2':
                    Add_product()
                elif choice == '3':
                    delete_product()
                elif choice == '4':
                    update_product()
                elif choice == '5':
                    findProd()
                elif choice == '6':
                    listSales()
                elif choice == '7':                    
                    print("Logging out...")
                    break
                else:
                    print("invalid choice.\n")
        elif admin_or_user in registered_users:
            while True:
                print("\n1. View all products")
                print("2. Search Product")
                print("3. View Cart")
                print("4. Add to Cart")
                print("5. Delete from Cart")
                print("6. Checkout")
                print("7. View Orders")
                print("8. Cash-in")
                print("9. View Balance")
                print("0. Log-out")
                choice = input()
                if choice == '1':
                    listProd()
                elif choice == '2':
                    findProd()
                elif choice == '3':
                    view_cart(admin_or_user)
                elif choice == '4':
                    add_to_cart(admin_or_user)
                elif choice == '5':
                    delete_cart(admin_or_user)
                elif choice == '6':
                    checkOut(admin_or_user)
                elif choice == '7':
                    view_orders(admin_or_user)
                elif choice == '8':
                    try:
                        val = input("How much pesos do you want to cash in? ")
                        admin_or_user[4] += int(val)
                    except:
                        print("invalid input")
                elif choice == '9':
                    print("Balance: ₱{:,.2f}".format(admin_or_user[4]))
                elif choice == '0':                    
                    print("Logging out...")
                    break
                else:
                    print("invalid choice.\n")
        elif admin_or_user == 3:
            continue
        else:
            print("User not Found :(\n")

main() # calls the main function for the code to run
