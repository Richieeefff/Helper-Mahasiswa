import time
from plyer import notification

class TimerModel:
    def __init__(self):
        self.pomodoro_enabled = False
        self.remaining_time = 0
        self.pomodoro_interval = 25 * 60  # 25 minutes
        self.break_duration = 5 * 60  # 5 minutes

    def send_notification(self, title, message):
        notification.notify(title=title, message=message)

    def countdown(self, seconds):
        self.remaining_time = seconds
        while self.remaining_time > 0:
            yield self.remaining_time
            time.sleep(1)
            self.remaining_time -= 1
