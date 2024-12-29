from views.profilViews import display_user_info
from views.loginViews import display_main_menu
from views.tipsViews import display_admin_panel
from views.jadwalkView import tampilan
from views.jadwaltViews import main_tugas
from views.timerViews import display_timer_setup
from views.tipsViews import display_main_panel
from views.profilViews import showProfile
import utils.helper as helper


def interface(username):
    helper.clear()
    while True:
        summary = display_user_info(username)
        helper.clear()
        print("========================================")
        print("|       HELPER MAHASISWA DASHBOARD     |")
        print("========================================")
        print("|                                      |")
        display_user_info(username)
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
            tampilan()
        elif pilihan == '3':
            main_tugas(username)
        elif pilihan == '4':
            display_timer_setup(username)
        elif pilihan == '5':
            display_main_panel()
        elif pilihan == '0':
            print("Terima kasih telah menggunakan Helper Mahasiswa!")
            exit()
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

