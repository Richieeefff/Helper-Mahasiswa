from utils import helper
from function import login
from function import (
    jadwalkuliah,
    tipsBelajar,
    jadwalTugas,
    timerBelajar,
    profil,
    dashboard
)

def interface(username):
    # Interface utama yang memuat semua fitur setelah user melakukan login
    while True:
        summary = dashboard.get_user_info(username)
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
            profil.showProfile(username)
        elif pilihan == '2':
            jadwalkuliah.main_jadwal(username)
        elif pilihan == '3':
            jadwalTugas.main_tugas(username)
        elif pilihan == '4':
            timerBelajar.timerSetup()
        elif pilihan == '5':
            tipsBelajar.main_panel()
        elif pilihan == '0':
            print("Terima kasih telah menggunakan Helper Mahasiswa!")
            exit()
        else:
            print("Opsi tidak valid! Silakan coba lagi.")

def main():
    while True:
        username = login.main()
        if username == "admin":
            tipsBelajar.admin_panel()
        elif username:
            interface(username)
    
if __name__ == "__main__":
    main()