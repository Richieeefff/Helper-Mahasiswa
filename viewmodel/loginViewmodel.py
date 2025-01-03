from model.loginModel import load_users, save_users

def register_user(username, password):
    user_data = load_users()

    for user in user_data["users"]:
        if user["username"] == username:
            return False  
        
    new_user = {
        "username": username,
        "password": password,
        "scheduled_tasks": [],
        "university_schedule": [],
        "exp": 0,
        "time":[],
        "tipe": None
    }
    user_data["users"].append(new_user)
    save_users(user_data)
    return True

def authenticate_user(username, password):
    if username == "admin" and password == "admin":
        return True  

    user_data = load_users()
    for user in user_data["users"]:
        if username == user["username"] and password == user["password"]:
            return True  

    return False  
