from data import load_projects

def view_projects(user):
    projects = load_projects()
    if not projects:
        print("No projects found.")
        return
    for p in projects:
        if p['user_id'] == user['id']:
            print(f"ID: {p['id']} | Title: {p['Title']} | Target: {p['Total Target']} | Start: {p['Start']} | End: {p['End']}")