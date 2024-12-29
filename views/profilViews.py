from viewmodel.profilViewmodel import get_user_info

def display_user_info(username):
    try:
        user_info = get_user_info(username)
        if username == "admin":
            print(f"Welcome, {user_info['username']}!")
            print("Admin does not have tasks or schedules.")
        else:
            print(user_info["welcome_message"])
            print(user_info["task_message"])    
            print(user_info["schedule_message"])
            print(user_info["week_hours"])
            print(user_info["tipe"])
    except ValueError as e:
        print(str(e))
