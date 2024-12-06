from model.timerModel import TimerModel

class TimerViewModel:
    def __init__(self):
        self.model = TimerModel()
        self.is_running = False

    def setup_timer(self, hours, minutes, pomodoro):
        total_seconds = (hours * 3600) + (minutes * 60)
        self.model.pomodoro_enabled = pomodoro
        return total_seconds

    def run_timer(self, total_seconds):
        self.is_running = True
        self.model.send_notification("⏰ Timer Belajar ⏰", "Timer Dimulai!")
        for remaining_time in self.model.countdown(total_seconds):
            yield remaining_time
        self.is_running = False
        self.model.send_notification("⏰ Timer Belajar ⏰", "Timer Selesai!")
