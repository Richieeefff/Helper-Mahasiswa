import utils.helper as helper
import time
from viewmodel.tipsViewModel import TipsViewModel

class TipsView:
    def __init__(self, username):
        self.viewmodel = TipsViewModel()
        self.username = username

    def admin_panel(self):
        while True:
            helper.clear()
            print("========================================")
            print("| No |          Admin Panel            |")
            print("========================================")
            print("| 1  | Tambah Tips                     |")
            print("| 2  | Lihat Tips                      |")
            print("| 0  | Keluar                          |")
            print("========================================")

            pilihan = input("Pilih opsi (0-2): ")
            if pilihan == '1':
                self.viewmodel.tambah_tips()
            elif pilihan == '2':
                tips = self.viewmodel.lihat_tips()
                if tips:
                    helper.clear()
                    for key, value in tips.items():  # Ensure lihat_tips returns a dictionary
                        print(f"Dari {key.title()}: \"{value.title()}\"")
                time.sleep(5)
            elif pilihan == '0':
                return
            else:
                print("Opsi tidak valid! Silakan coba lagi.")
    
    def tips_panel(self):
        while True:
            helper.clear()
            print("========================================")
            print("| No |          Tips Belajar           |")
            print("========================================")
            print("| 1  | Lihat Tips                      |")
            print("| 0  | Kembali                         |")
            print("========================================")

            pilihan = input("Pilih opsi (0-2): ")
            if pilihan == '1':
                tips = self.viewmodel.lihat_tips()
                if tips:
                    helper.clear()
                    for key, value in tips.items():  # Ensure lihat_tips returns a dictionary
                        print(f"Dari {key.title()}: \"{value.title()}\"")
                else:
                    print("Tidak ada tips untuk saat ini")
                time.sleep(5)
            elif pilihan == '0':
                return
            else:
                print("Opsi tidak valid! Silakan coba lagi.")

    def display_menu(self, username):
        if username == "admin":
            self.admin_panel()
        else:
            self.tips_panel()