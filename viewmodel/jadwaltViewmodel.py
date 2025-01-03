from model.jadwaltModel import load_user_data, save_user_data, find_user
from datetime import datetime

def add_task(username, matkul, judul, deskripsi, kesulitan, tenggat):
    data = load_user_data()
    tanggal = datetime.today().date()

    for user in data["users"]:
        if user["username"] == username:
            user["scheduled_tasks"].append({
                'tanggal': str(tanggal),
                'mata_kuliah': matkul,
                'judul': judul,
                'deskripsi': deskripsi,
                'tingkat_kesulitan': kesulitan,
                'tenggat': str(tenggat),
                'status': 'Belum Selesai'
            })
            save_user_data(data)
            return True
    return False

def get_tasks(username):
    user = find_user(username)
    if user:
        return user.get("scheduled_tasks", [])
    return []

def complete_task(username, task_index, status):
    data = load_user_data()
    for user in data["users"]:
        if user["username"] == username:
            if 0 <= task_index < len(user["scheduled_tasks"]):
                tugasPilihan = user["scheduled_tasks"][task_index - 1]
                user["scheduled_tasks"][task_index]["status"] = status
                diffExp = {"Mudah": 100, "Sedang": 200, "Sulit": 300}
                expGain = diffExp.get(tugasPilihan['tingkat_kesulitan'],0)
                user["exp"] = user.get("exp", 0) + expGain
                save_user_data(data)
                return True
    return False

def delete_task(username, task_index):
    data = load_user_data()
    for user in data["users"]:
        if user["username"] == username:
            if 0 <= task_index < len(user["scheduled_tasks"]):
                user["scheduled_tasks"].pop(task_index)
                save_user_data(data)
                return True
    return False
