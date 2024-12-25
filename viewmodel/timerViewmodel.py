import time
import utils.helper as helper
from model.timerModel import countdown, timerSetup

def set_time(jam, menit):
    menit = round(menit / 10) * 10  
    jam += menit // 60
    menit = menit % 60
    return jam, menit

def set_pomodoro(pomodoro_input):
    return pomodoro_input == "y"

def confirm_timer_setup(jam, menit, pomodoro):
    return input(f"Timer akan di set dengan waktu {jam} jam {menit} menit (pomodoro {pomodoro}). Lanjutkan? [Y/n] ").lower() == 'y'

def start_timer(jam, menit, pomodoro):
    timerSetup(jam, menit, pomodoro)
