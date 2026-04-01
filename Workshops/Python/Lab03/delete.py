import json
from data import load_projects, save_projects
from view import view_projects

def delete_project(user):
    view_projects(user)
    project_id = input("Enter Project ID to delete: ")
    projects = load_projects()
    for p in projects:
        if p["user_id"] == user["id"]:
            if p["id"] == project_id:
                projects.remove(p)
                with open("projects.json", "w") as f:
                    json.dump(projects, f, indent=4)
                print("Project deleted successfully!")
                return
    print("Project not found!")