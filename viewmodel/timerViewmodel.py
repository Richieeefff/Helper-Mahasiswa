from model.timerModel import timerSetup

def set_pomodoro(pomodoro_input):
    return pomodoro_input == "y"

def confirm_timer_setup(jam, menit, pomodoro):

    return input(f"Timer akan di set dengan waktu {jam} jam {menit} menit (pomodoro {pomodoro}). Lanjutkan? [Y/n] ").lower() == 'y'

def start_timer(jam, menit, pomodoro,username):
    timerSetup(jam, menit, pomodoro, username)
