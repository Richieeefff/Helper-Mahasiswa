import time
import utils.helper as helper

def countdown(seconds, pomodoro):
    pom = 0  # menit yang dilalui
    helper.clear()
    helper.send_notification("⏰ Timer Belajar ⏰", "Timer Dimulai!")
    print("Timer Dimulai")
    while seconds: 
        hours = seconds // 3600
        mins = (seconds % 3600) // 60
        secs = seconds % 60
        print(f"Waktu belajar [{hours:02}:{mins:02}:{secs:02}]   ", end="\r")
        if pomodoro: 
            if pom == 25:  # Setiap 25 menit
                print("Waktunya istirahat 5 menit!", end="\r")
                helper.send_notification("⏰ Pomodoro Timer ⏰", "Waktunya Istirahat 5 Menit!")
                time.sleep(5)
                pomTimer = 295  # 5 menit istirahat
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

def timerSetup(jam, menit, pomodoro):
        countdown((menit * 60) + (jam * 3600), pomodoro)
        return