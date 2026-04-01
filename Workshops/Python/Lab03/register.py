from validate import validate_mail, validate_name, validate_password, validate_phone
from data import save_users

def askforstr(message):
    while True:
        name = input(message)
        if validate_name(name):
            return name
        print("Invalid Name!")

def register():
    
    Fname = askforstr("Please Enter First Name: ")
    Lname = askforstr("Please Enter Last Name: ")
    
    while True:
        mail = input("Email: ")
        if validate_mail(mail):
            break
        print("Invalid Email!")
    while True:
        password = input("Password: ")
        if validate_password(password):
            break
        print("Invalid Password!")
    while True:
        confirm_pass = input("Confirm Password: ")
        if confirm_pass == password:
            break
        print("Passwords Do Not Match!")
    while True:
        mobile = input("Phone number: ")
        if validate_phone(mobile):
            break
        print("Invalid Phone Number!")
    
    user = {
        "first_name": Fname,
        "last_name": Lname,
        "email": mail,
        "password": password,
        "phone": mobile
    }

    save_users(user)
    print("Registeration Successful")

