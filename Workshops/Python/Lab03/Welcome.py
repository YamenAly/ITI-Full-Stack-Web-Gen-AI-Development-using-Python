from login import login
from register import register

def welcome_menu():
    while True:
        print("------------Welcome-------------")
        print("1.Already Have an Account, Login")
        print("2.Don't have an account? Register")
        x = input("Choice: ")
        if x == "1":
            login()
        elif x == "2":
            register()
        else:
            print("Invalid choice")