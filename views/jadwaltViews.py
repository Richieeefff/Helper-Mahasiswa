import time
import utils.helper as helper
from viewmodel.jadwaltViewmodel import add_task, get_tasks, complete_task, delete_task
from datetime import datetime

def penambahan(username):
    tanggal = datetime.today().date()
    matkul = helper.validate_alpha("Masukkan nama mata kuliah: ")
    judul = helper.validate_alnum("Masukkan judul tugas: ")
    deskripsi = helper.validate_alnum("Masukkan deskripsi tugas: ")

    while True:
        print("Pilih tingkat kesulitan tugas:")
        print("1. Mudah")
        print("2. Sedang")
        print("3. Sulit")
        diffChoice = input("Pilih opsi (1-3): ")
        if diffChoice == '1':
            kesulitan = "Mudah"
            break
        elif diffChoice == '2':
            kesulitan = "Sedang"
            break
        elif diffChoice == '3':
            kesulitan = "Sulit"
            break
        else:
            print("Opsi tidak valid! Silakan coba lagi.\n")
            time.sleep(1)
            helper.clear()

    while True:
        tenggat = helper.get_valid_date("\nMasukkan tanggal tenggat tugas (YYYY-MM-DD): ")
        if tenggat > tanggal:
            break
        else:
            print("Tanggal tenggat waktu lebih awal dari tanggal hari ini")

    if add_task(username, matkul, judul, deskripsi, kesulitan, tenggat):
        print("Tugas berhasil ditambahkan!\n")
    else:
        print(f"User {username} tidak ditemukan.")

def tampilan(username):
    tugas = get_tasks(username)
    if not tugas:
        print("Cie lagi gak ada tugas.\n")
        return

    print(f"Scheduled Tasks:")
    print("=" * 50)
    for i, tugas in enumerate(tugas, 1):
        print(f"Tugas {i}:")
        print(f"  - Tanggal: {tugas['tanggal']}")
        print(f"  - Mata_kuliah: {tugas['mata_kuliah']}")
        print(f"  - Judul: {tugas['judul']}")
        print(f"  - Deskripsi: {tugas['deskripsi']}")
        print(f"  - Kesulitan: {tugas['tingkat_kesulitan']}")
        print(f"  - Tenggat: {tugas['tenggat']}")
        print(f"  - Status: {tugas['status']}")
        print("=" * 50)

def selesaikanTugas(username):
    tampilan(username)
    tugas = get_tasks(username)
    if not tugas:
        return

    while True:
        try:
            tugasID = int(input("Pilih nomor tugas yang ingin diselesaikan: ")) - 1
            if 0 <= tugasID < len(tugas):
                statusBaru = input("Apakah tugas ini sudah selesai? [Y/n] ").strip().lower()
                if statusBaru == 'y':
                    complete_task(username, tugasID, 'Selesai')
                    print("Status berhasil diubah menjadi 'Selesai'!\n")
                    return
                elif statusBaru == 'n':
                    complete_task(username, tugasID, 'Belum Selesai')
                    print("Status berhasil diubah menjadi 'Belum Selesai'!\n")
                    return
                else:
                    print("Input tidak valid! Harap masukkan 'Y' untuk ya atau 'n' untuk tidak.")
            else:
                print("Tugas tidak ada. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid! Silakan coba lagi.")

def hapusTugas(username):
    tampilan(username)
    tugas = get_tasks(username)
    if not tugas:
        return

    while True:
        try:
            tugasID = int(input("Pilih nomor tugas yang ingin dihapus: ")) - 1
            if delete_task(username, tugasID):
                print("Tugas berhasil dihapus!")
                return
            else:
                print("ID tugas salah! Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid! Silakan coba lagi.")

def main_tugas(username):
    while True:
        helper.clear()
        print("========================================")
        print("| No |          Menu Tugas             |")
        print("========================================")
        print("| 1  | Menambahkan Tugas               |")
        print("| 2  | Melihat Tugas                   |")
        print("| 3  | Selesaikan Tugas                |")
        print("| 4  | Menghapus Tugas                 |")
        print("| 0  | Keluar                          |")
        print("========================================")
        
        pilihan = input("Pilih opsi (0-4): ")
        if pilihan == '1':
            helper.clear()
            penambahan(username)
            time.sleep(1)
        elif pilihan == '2':
            helper.clear()
            tampilan(username)
            time.sleep(3)
        elif pilihan == '3':
            helper.clear()
            selesaikanTugas(username)
            time.sleep(1)
        elif pilihan == '4':
            helper.clear()
            hapusTugas(username)
            time.sleep(1)
        elif pilihan == '0':
            return
        else:
            print("Opsi tidak valid! Silakan coba lagi.")
