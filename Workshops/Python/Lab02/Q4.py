# Ask the user for his name then confirm that he has entered his
# name(not an empty string/integers). then proceed to ask him for
# his email and print all this data (Bonus) check if it is a valid email or not

name = input("Enter your name: ")

while name.isdigit():
    print("Invalid input, enter letters only")
    name = input("Enter your name: ")

email = input("Enter your email: ")

while "@" not in email or "." not in email:
    print("Invalid email, please enter a valid email")
    name = input("Enter your name: ")

print("Name: ", name)
print("Email: ", email)
