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
        print("\tItem {}: {} (Quantity: {})".format(idx + 1, item[1], item[2]))
        for i in products:
            if item[0] == i[0]:
                total = total + (int(item[2])*i[4])
    print("Total Cost: {}".format(total))
    return
