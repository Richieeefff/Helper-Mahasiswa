import utils.helper as helper

def get_user_info(username):
    """Retrieve user information, including task and schedule counts."""
    if username == "admin":
        return {
            "username": username,
            "task_count": None,
            "schedule_count": None,
        }
    user = helper.find_user(username)
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