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

    # more information details can be implemented if necessary

    r_credentials = [r_username, r_password]

    registered_users.append(r_credentials)
    print("Successfully registered! Now please log in :)")
    return 3


# MAIN FUNCTION
def main():
    while True:
        print("Sales Inventory System")

        user_input = input("(1) Log-In or (2) Register (Enter #): ")

        if user_input.isdigit():
            if int(user_input) == 1:
                admin_or_user = log_in()
            elif int(user_input) == 2:
                admin_or_user = register()
            else:
                print("Invalid input. Please try again :(\n")
                continue
        else:
            print("Invalid input. Please try again :(\n")
            continue
        if admin_or_user == 1:
            print("Access to all admin functions")
        elif admin_or_user == 2:
            print("Access to all registered user functions")
        elif admin_or_user == 3:
            continue
        else:
            print("User not Found :(\n")

main() # calls the main function for the code to run
