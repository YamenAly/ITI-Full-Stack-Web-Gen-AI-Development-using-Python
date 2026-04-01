from validate import validate_mail, validate_password
from data import load_users
from projects import projects_menu

def login():
    users = load_users()
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
    
    for user in users:
        if user["email"] == mail:
            if user["password"] == password:
                print("Login Successful")
                projects_menu(user)
            else:
                print("Wrong Password")
                return None
    print("Email not found!")
    return None