import time
from viewmodel.timerViewmodel import set_time, set_pomodoro, confirm_timer_setup, start_timer
import utils.helper as helper

def display_timer_setup():
    helper.clear()
    print("Tentukan waktu timer (Interval 10 menit)")
    
    while True:
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
        if pomodoro_input in ['y', 'n']:
            break
        else:
            print("Input invalid! Harap masukkan 'Y' untuk ya atau 'n' untuk tidak.")
    
    
    jam, menit = set_time(jam, menit)
    
   
    pomodoro = set_pomodoro(pomodoro_input)


    if confirm_timer_setup(jam, menit, pomodoro):
        start_timer(jam, menit, pomodoro)
