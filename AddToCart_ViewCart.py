cart = []

# ADD TO CART METHOD 
def add_to_cart():
    print("\nAdd To Cart") 
    while True:
        input_item = input("Please Enter a Valid Product ID: ")
        for idx, item in enumerate(products):
            if input_item.upper() == products[idx][0]:
                input_itemno = int(input("How many product do you want to add to cart: "))
                if input_itemno <= products[idx][3]:
                    products[idx][3] = products[idx][3] - input_itemno
                    newcart = [username,products[idx][1],input_itemno]
                    cart.append(newcart)
                    print("{} {} successfully added to cart! :)\n".format(input_itemno, products[idx][2]))
                    return
        print("Invalid input. Please try again :(\n")


# VIEW CART METHOD / SHOW ITEMS IN THE CART METHOD
def view_cart():
    print("\nView Cart")

    print("You have {} item/s in the cart: ".format(len(cart)))
    for idx, item in enumerate(cart):
        if username == cart[idx][0]:
            print("\tItem {}: {} {}".format(idx + 1, item[2], item[1]))
    return
