from model.menuModel import MenuModel

class MenuViewModel:
    def __init__(self, username):
        self.model = MenuModel(username)

    def get_dashboard_summary(self):
        """Prepare dashboard data for display."""
        summary = self.model.get_user_info()
        return {
            "username": f"{summary['username']}",
            "welcome_message": f"Selamat datang, {summary['username']}!",
            "task_message": f"Kamu mempunyai {summary['task_count']} tugas pending.",
            "schedule_message": f"{summary['schedule_count']} jadwal kuliah hari ini.",
        }
