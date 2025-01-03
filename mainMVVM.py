from views.profilViews import *
from views.loginViews import *
from views.tipsViews import *
from views.jadwalkView import *
from views.jadwaltViews import *
from views.timerViews import *
import utils.helper as helper
import time
import sys


def interface(username):
    helper.clear()
    while True:
        summary = display_user_info(username)
        helper.clear()
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
            showProfile(username)
        elif pilihan == '2':
            main_jadwal(username)
        elif pilihan == '3':
            main_tugas(username)
        elif pilihan == '4':
            display_timer_setup(username)
        elif pilihan == '5':
            display_main_panel()
        elif pilihan == '0':
            print("Terima kasih telah menggunakan Helper Mahasiswa!")
            time.sleep(1)
            sys.exit()
        else:
            print("Opsi tidak valid! Silakan coba lagi.")
    

def main():
    while True:
        username = display_main_menu()
        if username == "admin":
            display_admin_panel()
        elif username:
            interface(username)

if __name__ == "__main__":
    main()

