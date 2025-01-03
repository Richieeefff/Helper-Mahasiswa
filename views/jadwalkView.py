from prettytable import PrettyTable
from viewmodel import jadwalkViewmodel
import utils.helper as helper
import time

def main_jadwal(username):
    while True:
        helper.clear()
        print("========================================")
        print("| No |         Jadwal Kuliah           |")
        print("========================================")
        print("| 1  | Tambah Jadwal Kuliah            |")
        print("| 2  | Tampilkan Jadwal Kuliah         |")
        print("| 3  | Hapus Jadwal Kuliah             |")
        print("| 4  | Edit Jadwal Kuliah              |")
        print("| 0  | Keluar                          |")
        print("========================================")
        
        pilihan = input("Pilih menu (0-4): ")
        
        if pilihan == "1":
            helper.clear()
            jadwalkViewmodel.penambahan(username)
            time.sleep(1)
        elif pilihan == "2":
            helper.clear()
            jadwalkViewmodel.tampilan(username)
            time.sleep(1)
        elif pilihan == "3":
            helper.clear()
            jadwalkViewmodel.hapusJadwal(username)
            time.sleep(1)
        elif pilihan == "4":
            helper.clear()
            jadwalkViewmodel.editJadwal(username)
            time.sleep(1)
        elif pilihan == "0":
            return
        else:
            print("Opsi tidak valid! Silakan coba lagi.")