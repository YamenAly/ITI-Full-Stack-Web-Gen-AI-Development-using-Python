from create import create_project
from view import view_projects
from edit import edit_project
from delete import delete_project
from search import search_project

def projects_menu(user):
    while True:
        print("------Project-------")
        print("1. Create Project")
        print("2. View Projects")
        print("3. Edit Project")
        print("4. Delete Project")
        print("5. Search Project")
        print("6. Logout")
        x = input("Choice: ")
        if x == "1":
            create_project(user)
        elif x == "2":
            view_projects(user)
        elif x == "3":
            edit_project(user)
        elif x == "4":
            delete_project(user)
        elif x == "5":
            search_project(user)
        elif x == "6":
            return
        else:
            print("Invalid choice")
