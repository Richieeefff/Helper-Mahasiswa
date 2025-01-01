import utils.helper as helper
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, "id_ID.UTF-8") # Set ke Indonesia

def get_date():
    today = datetime.now()
    day = today.strftime("%A")

    return day

def get_user_info(username):
    
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