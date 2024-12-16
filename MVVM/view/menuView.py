import utils.helper as helper
import time
from viewmodel.menuViewModel import MenuViewModel
from view.timerView import TimerView
from view.tipsView import TipsView
from view.tugasView import TugasView
from view.jadwalView import JadwalView

class MenuView:
    def __init__(self, username):
        self.viewmodel = MenuViewModel(username)
        self.timerview = TimerView()
        self.tipsview = TipsView(username)
        self.tugasview = TugasView(username)

    def display_menu(self):
        while True:
            summary = self.viewmodel.get_dashboard_summary()
            helper.clear()
            if summary["username"] == "admin":
                self.tipsview.display_menu("admin")
                return
            else:
                print("========================================")
                print("|       HELPER MAHASISWA DASHBOARD     |")
                print("========================================")
                print("|                                      |")
                print(f"| {summary['welcome_message']:<37}|")
                print(f"| {summary['task_message']:<37}|")
                print(f"| {summary['schedule_message']:<37}|")
                print("|                                      |")
                print("========================================")
                print("| No |             Menu                |")
                print("========================================")
                print("| 1  | Profil                          |")
                print("| 2  | Jadwal Kuliah                   |")
                print("| 3  | Jadwal Tugas                    |")
                print("| 4  | Timer Belajar                   |")
                print("| 5  | Tips Belajar                    |")
                print("| 0  | Keluar                          |")
                print("========================================")
            
                pilihan = input("Pilih opsi (0-5): ")
                if pilihan == '1':
                    print("This feature is coming soon")
                    time.sleep(3)
                elif pilihan == '2':
                    self.jadwalview.jadwal()
                elif pilihan == '3':
                    self.tugasview.display()
                elif pilihan == '4':
                    self.timerview.start_timer()
                elif pilihan == '5':
                    self.tipsview.display_menu(summary["username"])
                elif pilihan == '0':
                    print("Terima kasih telah menggunakan Helper Mahasiswa!")
                    exit()
                else:
                    print("Opsi tidak valid! Silakan coba lagi.")