from model.profilModel import find_user

def get_user_info(username):
    if username == "admin":
        return {
            "username": username,
            "task_count": None,
            "schedule_count": None,
        }
    user = find_user(username)
    if user:
        task_count = len(user["scheduled_tasks"])
        schedule_count = len(user["university_schedule"])
        return {
            "welcome_message": f"Selamat datang, {username}!",
            "task_message": f"Kamu mempunyai {task_count} tugas pending.",
            "schedule_message": f"{schedule_count} jadwal kuliah hari ini.",
        }
    else:
        raise ValueError("User not found.")
