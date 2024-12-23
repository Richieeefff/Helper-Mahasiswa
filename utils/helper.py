import os
import json
from plyer import notification

DATA_FILE = "user_data.json"

def clear():
    # Cek OS dan clear terminal
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # MacOS/Linux
        os.system('clear')

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Helper Mahasiswa", 
        timeout=5  # Durasi notifikasi
    )

def load_user_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_user_data(user_data):
    with open(DATA_FILE, 'w') as file:
        json.dump(user_data, file, indent=4)

def find_user(username):
    """Find the user by username."""
    user_data = load_user_data()
    for user in user_data["users"]:
        if user["username"] == username:
            return user
    return None