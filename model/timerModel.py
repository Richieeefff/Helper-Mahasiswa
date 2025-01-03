import time
import keyboard  
import threading
import utils.helper as helper
from model.profilModel import find_user
from utils.helper import load_user_data, save_user_data
from datetime import datetime


paused = False
stopped = False

def save_timer(seconds, username):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sumMinutes = seconds / 60
    
    if sumMinutes == int(sumMinutes):
        sumMinutes = int(sumMinutes)
    else:
        sumMinutes = round(sumMinutes, 2)

    user = find_user(username)
    data = load_user_data()

    for user in data["users"]:
        if user["username"] == username:
            
            user["time"].append({
                "date": current_date,
                "sum_of_minutes": sumMinutes
            })
            save_user_data(data)


def countdown(seconds, pomodoro, username):
    global paused, stopped
    pom = 0  
    helper.clear()
    helper.send_notification("⏰ Timer Belajar ⏰", "Timer Dimulai!")
    print("Timer Dimulai")
    print("Tekan 'shift' untuk pause atau 'ctrl' untuk berhenti.")

    second_awal = seconds

    while seconds and not stopped:
        if paused:
            print("Timer Dijeda... Tekan 'shift' untuk melanjutkan atau 'ctrl' untuk berhenti.   ", end="\r")
            time.sleep(1)
            continue
        
        hours = seconds // 3600
        mins = (seconds % 3600) // 60
        secs = seconds % 60
        print(f"Waktu belajar [{hours:02}:{mins:02}:{secs:02}]                                                      ", end="\r")

        if pomodoro:
            if pom == 25:  # Every 25 minutes
                print("Waktunya istirahat 5 menit!", end="\r")
                helper.send_notification("⏰ Pomodoro Timer ⏰", "Waktunya Istirahat 5 Menit!")
                time.sleep(5)
                pomTimer = 295  # 5-minute break
                while pomTimer and not stopped:
                    if paused:
                        print("Istirahat Dijeda... Tekan 'shift' untuk melanjutkan atau 'ctrl' untuk berhenti.   ", end="\r")
                        time.sleep(1)
                        continue
                    pomMins = pomTimer // 60
                    pomSecs = pomTimer % 60
                    print(f"Waktu istirahat [{pomMins:02}:{pomSecs:02}]                                                         ", end="\r")
                    time.sleep(1)
                    pomTimer -= 1
                pom = 0
                if stopped:
                    save_timer(second_awal - seconds,username)
                    return
                print("Istirahat selesai!         ", end="\r")
                helper.send_notification("⏰ Pomodoro Timer ⏰", "Istirahat Selesai! Saatnya FOKUS kembali")
                time.sleep(5)
                continue
        time.sleep(.001)
        seconds -= 1
        if seconds % 60 == 0 and pomodoro:
            pom += 1
    if not stopped:
        print("Waktu Belajar Habis!    ")
        helper.send_notification("⏰ Timer Belajar ⏰", "Timer Selesai!")
        save_timer(second_awal,username)
        time.sleep(5)
    save_timer(second_awal - seconds,username)
    return



def monitor_keys():
    global paused, stopped
    while not stopped:
        if keyboard.is_pressed('shift'):
            paused = not paused
            time.sleep(0.5)  
        if keyboard.is_pressed('ctrl'):
            stopped = True
        time.sleep(0.1)  

def timerSetup(jam, menit, pomodoro, username):
    global paused, stopped
    paused = False
    stopped = False

    
    timer_thread = threading.Thread(target=countdown, args=((menit * 60) + (jam * 3600), pomodoro, username))
    monitor_thread = threading.Thread(target=monitor_keys)
    
    timer_thread.start()
    monitor_thread.start()

    timer_thread.join()
    monitor_thread.join()
