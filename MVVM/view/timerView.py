import utils.helper as helper
from viewmodel.timerViewModel import TimerViewModel
import time

class TimerView:
    def __init__(self):
        self.viewmodel = TimerViewModel()

    def display_timer(self, seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        print(f"Waktu belajar [{hours:02}:{minutes:02}:{seconds:02}]   ", end="\r")

    def get_timer_input(self):
        while True:
            helper.clear() 
            print("Tentukan waktu timer (Interval 10 menit)")
            try:
                hours = int(input("Jam: "))
                minutes = round(int(input("Menit: ")) / 10) * 10
                hours += minutes // 60
                minutes = minutes % 60
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
            confirm = input(f"Timer akan di set dengan waktu {hours} jam {minutes} menit (pomodoro {pomodoro}). Lanjutkan? [Y/n] ")
            if confirm.lower() == "y": 
                return hours, minutes, pomodoro
            elif confirm.lower() == "n": 
                return None, None, None
            else:
                print("Input invalid! Harap masukkan 'Y' untuk ya atau 'n' untuk tidak.")    

    def start_timer(self):
        hours, minutes, pomodoro = self.get_timer_input()
        if minutes is not None:
            total_seconds = self.viewmodel.setup_timer(hours, minutes, pomodoro)
            for remaining_time in self.viewmodel.run_timer(total_seconds):
                self.display_timer(remaining_time)
            print("\nWaktu Belajar Habis!")
        else: 
            return

if __name__ == "__main__":
    view = TimerView()
    view.start_timer()
