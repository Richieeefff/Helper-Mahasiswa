from model.profilModel import find_user
from utils.helper import load_user_data
import locale
from datetime import datetime

def get_study_type(week_hours):
    if week_hours <= 5:
        return "Pemula: Belajar dengan sedikit usaha dan waktu."
    elif 5 < week_hours <= 10:
        return "Belajar Kasual: Belajar cukup santai, belum terlalu fokus."
    elif 10 < week_hours <= 15:
        return "Belajar Reguler: Belajar dengan cukup disiplin."
    elif 15 < week_hours <= 20:
        return "Belajar Fokus: Fokus pada topik tertentu, belajar lebih intensif."
    elif 20 < week_hours <= 25:
        return "Belajar Konsisten: Menghabiskan waktu belajar yang cukup teratur."
    elif 25 < week_hours <= 30:
        return "Belajar Intensif: Sangat terorganisir dan berkomitmen tinggi."
    elif 30 < week_hours <= 35:
        return "Belajar Keras: Belajar dengan tekad tinggi, berusaha keras."
    elif 35 < week_hours <= 40:
        return "Belajar Terencana: Semua waktu belajar sangat terstruktur."
    elif 40 < week_hours <= 45:
        return "Belajar Rajin: Belajar sangat rajin dan penuh dedikasi."
    else:
        return "Belajar Sangat Keras: Belajar hampir sepanjang waktu, sangat ambisius."

def get_user_info(username):
    if username == "admin":
        return {
            "username": username,
            "task_count": None,
            "schedule_count": None,
        }
    user = find_user(username)
    if user:

        weekly_totals = {}

        for time_entry in user["time"]:
            date_str = time_entry["date"]
            sum_minutes = time_entry["sum_of_minutes"]

            date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
            year_week = f"{date_obj.year}-W{date_obj.isocalendar().week}"  

            if year_week not in weekly_totals:
                weekly_totals[year_week] = 0
            weekly_totals[year_week] += sum_minutes

        database = load_user_data()

        task_count = sum(
                            1 for user in database["users"]
                            for task in user.get("scheduled_tasks", [])
                            if task.get("status") == "Belum Selesai"
                        )
        schedule_count = jadwal_hariini(user["university_schedule"])
        week_hours = {week: total_minutes / 60 for week, total_minutes in weekly_totals.items()}


        if week_hours:
            latest_week = sorted(week_hours.keys(), reverse=True)[0]
            week_hours_value = week_hours.get(latest_week, 0)
        else:
            week_hours_value = 0

        study_type = get_study_type(week_hours_value)

        return {
            "welcome_message": f"Selamat datang, {username}!",
            "task_message": f"Kamu mempunyai {task_count} tugas pending.",
            "schedule_message": f"{schedule_count} jadwal kuliah hari ini.",
            "week_hours": f"Kamu sudah belajar selama {week_hours_value:.2f} jam di minggu ini.",
            "tipe": f"tipe belajar kamu adalah {study_type}"
        }
    else:
        raise ValueError("User not found.")

def jadwal_hariini(jadwal):
    # Set the locale ke Indonesia
    locale.setlocale(locale.LC_TIME, "id_ID.UTF-8")

    hari = datetime.now().strftime("%A")
    
    for day in jadwal:
        if day["hari"] == hari:
            return len(day["jadwal"]) 
    return "Tidak ada"    