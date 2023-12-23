import re

def check_email(email):
    """Check if the email is valid"""
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):  
        return True  
    else:  
        return False

def get_input():
    """Get the input from the user"""
    return input("Enter an email: ")

def main():
    """Main function of the program"""
    email = get_input()
    if check_email(email):
        print("The email is valid")
    else:
        print("The email is not valid")

if __name__ == "__main__":
    main()