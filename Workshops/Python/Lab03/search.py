from data import load_projects

def search_project(user):
    date = input("Enter date to search (yyyy-mm-dd): ")
    projects = load_projects()
    found = False
    for p in projects:
            if p["user_id"] == user["id"]:
                if p["Start"] <= date <= p["End"]:
                    print(f"ID: {p['id']} | Title: {p['Title']} | Target: {p['Total Target']} | Start: {p['Start']} | End: {p['End']}")                
                    found = True
    if not found:
        print("No projects found for that date.")