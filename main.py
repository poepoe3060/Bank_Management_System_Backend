from register import *

print("Welcome to my Testing Bank Project")
while True:
    try:
        register = int(input("1. Sign Up \n"
                             "2. Sign In "))
        if register == 1 or register == 2:
            if register == 1:
                SignUp()
        else:
            print("Please enter valid inputs from options.")
    except ValueError:
        print("Invalid input try again please.")