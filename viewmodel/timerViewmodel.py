from model.timerModel import countdown, timerSetup
from model.profilModel import find_user
from utils.helper import load_user_data, save_user_data
from datetime import datetime

def set_time(jam, menit):
    menit = round(menit / 10) * 10  
    jam += menit // 60
    menit = menit % 60

    return jam, menit

def set_pomodoro(pomodoro_input):
    return pomodoro_input == "y"

def confirm_timer_setup(jam, menit, pomodoro):

    return input(f"Timer akan di set dengan waktu {jam} jam {menit} menit (pomodoro {pomodoro}). Lanjutkan? [Y/n] ").lower() == 'y'

def start_timer(jam, menit, pomodoro,username):

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sumMinutes = jam * 60 + menit

    user = find_user(username)
    data = load_user_data()

    for user in data["users"]:
        if user["username"] == username:
            
            user["time"].append({
                "date": current_date,
                "sum_of_minutes": sumMinutes
            })
            save_user_data(data)


    timerSetup(jam, menit, pomodoro)
