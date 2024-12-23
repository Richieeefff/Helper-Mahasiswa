import utils.helper as helper
from datetime import datetime
import time

def penambahan(username):
    
    tanggal = datetime.today().date()
    matkul = helper.validate_isalpha("Masukkan nama mata kuliah: ")
    judul = helper.validate_isalnum("Masukkan judul tugas: ")
    deskripsi = helper.validate_isalnum("Masukkan deskripsi tugas: ")
    while True:
            print("Pilih tingkat kesulitan tugas:")
            print("1. Mudah")
            print("2. Sedang:")
            print("3. Sulit")
            diffChoice = input("Piling opsi (1-3): ")
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
        tenggat = helper.get_valid_date("\nMasukkan tanggal tenggat tugas (YYYY-MM-DD):")
        if tenggat > tanggal:
            break
        else:
            print("Tanggal tengat waktu lebih awal dari tanggal hari ini")

    database = helper.load_user_data()
    for user in database["users"]:
        if user["username"] == username:
            user["scheduled_tasks"].append({
                                    'tanggal': str(tanggal),
                                    'mata_kuliah': matkul, 
                                    'judul': judul,
                                    'deskripsi': deskripsi,
                                    'tingkat_kesulitan': kesulitan,
                                    'tenggat': str(tenggat),
                                    'status':'Belum Selesai'
                                    })
            helper.save_user_data(database)
            print("Tugas berhasil ditambahkan!\n")
            return
    print(f"User {username} not found.")


def tampilan(username):
    user = helper.find_user(username)
    tugas = user.get("scheduled_tasks", [])

    if not tugas:
        print("Cie lagi gak ada tugas.\n")
        return

    print(f"Username: {user['username']}\n")
    print("Scheduled Tasks:")
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
    data = helper.load_user_data()
    tampilan(username)
    for user in data["users"]:
        if user["username"] == username:
            while True:
                try:
                    tugasID = int(input("Pilih nomor tugas yang ingin diselesaikan: "))
                except ValueError:
                    print("Input tidak valid! Silakan coba lagi.")

                if 1 <= tugasID <= len(user["scheduled_tasks"]):
                    tugasPilihan = user["scheduled_tasks"][tugasID - 1]
                    print(f"Status tugas '{tugasPilihan['judul']}' saat ini: {tugasPilihan['status']}\n")
                    statusBaru = input("Apakah tugas ini sudah selesai? [Y/n] ").strip().lower()
                    if statusBaru == 'y':
                        tugasPilihan['status'] = 'Selesai'
                        helper.save_user_data(data)
                        print("Status berhasil diubah menjadi 'Selesai'!\n")
                        return
                    elif statusBaru == 'n':
                        tugasPilihan['status'] = 'Belum Selesai'
                        helper.save_user_data(data)
                        print("Status berhasil diubah menjadi 'Belum Selesai'!\n")
                        return
                    else:
                        print("Input tidak valid! Harap masukkan 'Y' untuk ya atau 'n' untuk tidak.")
                else:
                    print("Tugas tidak ada. Silakan coba lagi")
                    time.sleep(1)


def hapusTugas(username):
    database = helper.load_user_data()
    tampilan(username)

    for user in database["users"]:
        if user["username"] == username:
            while True:
                try:
                    tugasID = int(input("Pilih nomor tugas yang ingin dihapus: "))
                except ValueError:
                    print("Input tidak valid! Silakan coba lagi.")

                if 1 <= tugasID <= len(user["scheduled_tasks"]):
                    remove = user["scheduled_tasks"].pop(tugasID - 1)
                    helper.save_user_data(database)
                    print(f"Tugas {remove['judul']} berhasil dihapus")
                    return
                else:
                    print("ID tugas salah! Silahkan coba lagi.")

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
        
        pilihan = input("Pilih opsi (0-3): ")
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