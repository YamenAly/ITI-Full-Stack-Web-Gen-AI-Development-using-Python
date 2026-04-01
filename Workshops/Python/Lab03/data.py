import json, uuid

def load_users():
    try:
        with open("users.json" , "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_users(user: dict):
     try:
            users =  load_users()
            
            user["id"] = str(uuid.uuid4())
            
            users.append(user)
            with open("users.json" , "w") as f:
                 json.dump(users, f, indent=4)
            
            return True

     except Exception as e:
        print("Error: ", e)
        return  False
     
def load_projects():
    try:
        with open("projects.json" , "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
     
def save_projects(project: dict, user: dict):
    try:
            projects =  load_projects()
            
            project["id"] = str(uuid.uuid4())
            project["user_id"] = user["id"]
            
            projects.append(project)
            with open("projects.json" , "w") as f:
                 json.dump(projects, f, indent=4)
            
            return True
    
    except Exception as e:
        print("Error: ", e)
        return  False
     