from validate import validate_name, validate_date
from data import save_projects
import datetime

def askfordate(message):
    while True:
        date = input(message)
        if validate_date(date):
            return date
        print("Invalid date!")

def create_project(user):
    while True:
        title = input("Enter Project Title: ")
        if validate_name(title):
            break
        print("Invalid Title!")
    while True:
        details = input("Enter Project Details: ")
        if len(details) > 20:
            break
        else:
            print("Details too short")
    while True:
        target = input("Enter your Total Target: ")
        if target.isdigit():
            break
        else:
            print("Invalid target!")
    start = askfordate("Enter Start Date(yyyy-mm-dd): ")
    while True:
        end =  askfordate("Enter End Date(yyyy-mm-dd): ")
        if end > start:
            break
        else:
            print("End date must be after start date!")
    
    project = {
        "Title" : title,
        "Details" : details,
        "Total Target" : target,
        "Start" : start, 
        "End" : end
    }

    save_projects(project, user)
    print("Project Created Successfully!")