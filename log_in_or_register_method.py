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

        credentials = [username, password]
        
        if credentials in admin_users:
            print("Admin User: {}".format(username))
            return 1 
        elif credentials in registered_users:
            print("Registered User: {}".format(username))
            return 2 
        else:
            print("User not found. Try again :(\n")
    
# REGISTER METHOD
def register(): # admin registers are closed, no outside user can be an admin
    print("\nRegister") 
    r_username = input("Enter your username: ")
    r_password = input("Enter password: ")
    # more information details can be implemented if necessary

    r_credentials = [r_username, r_password]

    registered_users.append(r_credentials)
    print("Successfully registered! Now please log in :)\n")
    user_prompt()
    return 

# USER PROMPT METHOD (Log in or register)
def user_prompt():
    user_input = input("(1) Log-In or (2) Register (Enter #): ")

    if user_input.isdigit():
        if int(user_input) == 1:
            return_value = log_in()
        elif int(user_input) == 2:
            return_value = register()
        else:
            print("Invalid input. Please try again :(\n")
            user_prompt()
    else:
        print("Invalid input. Please try again :(\n")
        user_prompt()
    return return_value

# MAIN FUNCTION
def main():
    print("Sales Inventory System")

    # prompt the user if they want to log-in or register
    admin_or_user = user_prompt()

    if admin_or_user == 1:
        print("Access to all admin functions")
    elif admin_or_user == 2:
        print("Access to all registered user functions")
    else:
        print("Something went wrong. Please try again :(\n")
        user_prompt()

main() # calls the main function for the code to run
