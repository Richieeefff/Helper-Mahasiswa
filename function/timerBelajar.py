import time
from plyer import notification
import utils.helper as helper

def countdown(seconds, pomodoro):
    pom = 0 # menit yang dilalui
    helper.clear()
    helper.send_notification("⏰ Timer Belajar ⏰", "Timer Dimulai!")
    print("Timer Dimulai")
    while seconds: 
        hours = seconds // 3600
        mins = (seconds % 3600) // 60
        secs = seconds % 60
        print(f"Waktu belajar [{hours:02}:{mins:02}:{secs:02}]   ", end="\r")
        if pomodoro: 
            if pom == 25: # Setiap 25 menit
                print("Waktunya istirahat 5 menit!", end="\r")
                helper.send_notification("⏰ Pomodoro Timer ⏰", "Waktunya Istirahat 5 Menit!")
                time.sleep(5)
                pomTimer = 295 # 5 menit istirahat
                while pomTimer:
                    pomMins = pomTimer // 60
                    pomSecs = pomTimer % 60
                    print(f"Waktu istirahat [{pomMins:02}:{pomSecs:02}]    ", end="\r")
                    time.sleep(1)
                    pomTimer -= 1
                pom = 0
                print("Istirahat selesai!         ", end="\r")
                helper.send_notification("⏰ Pomodoro Timer ⏰", "Istirahat Selesai! Saatnya FOKUS kembali")
                time.sleep(5)
                continue
        time.sleep(1)
        seconds -= 1
        if seconds % 60 == 0 and pomodoro:
            pom += 1
    
    helper.clear()
    print("Waktu Belajar Habis!    ")
    helper.send_notification("⏰ Timer Belajar ⏰", "Timer Selesai!")
    time.sleep(5)
    return

def timerSetup():
    while True:
        helper.clear()
        print("Tentukan waktu timer (Interval 10 menit)")
        try:
            jam = int(input("Jam: "))
            menit = round(int(input("Menit: ")) / 10) * 10
            jam += menit // 60
            menit = menit % 60
            break
        except ValueError:
            print("Input anda tidak valid! Silahkan coba lagi.\n")
            time.sleep(3)
    
    while True:
        pomodoro_input = input("Gunakan pomodoro timer (setiap 25 menit istirahat 5 menit)? [Y/n] ").strip().lower()
        if pomodoro_input == "y":
            pomodoro = True
            break
        elif pomodoro_input == "n":
            pomodoro = False
            break
        else:
            print("Input invalid! Harap masukkan 'Y' untuk ya atau 'n' untuk tidak.")

    while True:
        confirm = input(f"Timer akan di set dengan waktu {jam} jam {menit} menit (pomodoro {pomodoro}). Lanjutkan? [Y/n] ")
        if confirm.lower() == "y": 
            countdown((menit*60) + (jam*3600), pomodoro)
            return
        elif confirm.lower() == "n": 
            return
        else:
            print("Input invalid! Harap masukkan 'Y' untuk ya atau 'n' untuk tidak.")    