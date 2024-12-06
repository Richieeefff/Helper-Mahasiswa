import time
from utils import helper
from function import login
from function import (
    jadwalkuliah,
    timerBelajar,
    tipsBelajar,
    jadwalTugas
)

def showDashboard():
    while True:
        print("========================================")
        print("|       HELPER MAHASISWA DASHBOARD     |")
        print("========================================")
        print("| No |           Menu                  |")
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
            profil()
        elif pilihan == '2':
            jadwalkuliah()
        elif pilihan == '3':
            jadwalTugas()
        elif pilihan == '4':
            timerBelajar()
        elif pilihan == '5':
            tipsBelajar()
        elif pilihan == '0':
            print("Terima kasih telah menggunakan Helper Mahasiswa!")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")