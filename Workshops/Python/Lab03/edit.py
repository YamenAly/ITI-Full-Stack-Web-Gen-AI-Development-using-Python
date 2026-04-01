import json
from data import load_projects, save_projects
from validate import validate_name
from create import askfordate
from view import view_projects

def edit_project(user):
    view_projects(user)
    project_id = input("Enter Project ID to edit: ")
    projects = load_projects()
    for p in projects:
        if p["user_id"] == user["id"]:
            if p["id"] == project_id:
                while True:
                    title = input("Enter New Project Title: ")
                    if validate_name(title):
                        break
                    print("Invalid Title!")
                while True:
                    details = input("Enter New Project Details: ")
                    if len(details) > 20:
                        break
                    else:
                        print("Details too short")
                while True:
                    target = input("Enter your New Total Target: ")
                    if target.isdigit():
                        break
                    else:
                        print("Invalid target!")
                start = askfordate("Enter New Start Date(yyyy-mm-dd): ")
                while True:
                    end =  askfordate("Enter New End Date(yyyy-mm-dd): ")
                    if end > start and end > p["Start"]:
                        break
                    else:
                        print("End date must be after start date!")
                p["Title"] = title
                p["Details"] = details
                p["Total Target"] = target
                p["Start"] = start
                p["End"] = end
                with open("projects.json" , "w") as f:
                    json.dump(projects, f, indent=4)
                print("Project Updated Successfully!")
                return
    print("Project not found!")
            


