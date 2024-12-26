import utils.helper as helper
from prettytable import PrettyTable
import time

def validasi_hari():
    hari_valid = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    
    while True:
        hari = input("Masukkan hari (Senin, Selasa, dst): ").capitalize()
        if hari in hari_valid:
            return hari
        else:
            print("Input tidak valid! Hari harus antara Senin hingga Minggu.")

def validasi_waktu():
    while True:
        waktu = input("Masukkan waktu (misal: 08:00 - 10:00): ")
     
        if " - " in waktu:
            start_time, end_time = waktu.split(" - ")
           
            if len(start_time) == 5 and len(end_time) == 5 and start_time[2] == ':' and end_time[2] == ':':
                start_hour, start_minute = start_time.split(":")
                end_hour, end_minute = end_time.split(":")
                
                if start_hour.isdigit() and start_minute.isdigit() and end_hour.isdigit() and end_minute.isdigit():
                    start_hour, start_minute, end_hour, end_minute = map(int, [start_hour, start_minute, end_hour, end_minute])
                    
                    if (0 <= start_hour < 24 and 0 <= start_minute < 60 and 
                        0 <= end_hour < 24 and 0 <= end_minute < 60):
                        return waktu
                    else:
                        print("Waktu tidak valid! Pastikan jam antara 00-23 dan menit antara 00-59.")
                else:
                    print("Jam dan menit harus berupa angka!")
            else:
                print("Format waktu tidak valid! Gunakan format HH:MM - HH:MM.")
        else:
            print("Format waktu tidak valid! Gunakan format HH:MM - HH:MM.")

def validasi_mata_kuliah():
    while True:
        matkul = input("Masukkan nama mata kuliah: ")
        if matkul.isalpha():
            return matkul
        else:
            print("Input tidak valid! Nama mata kuliah hanya boleh berisi huruf.")

def penambahan(username):
    database = helper.load_user_data()
    user = next((user for user in database["users"] if user["username"] == username), None)

    if not user:
        print("User tidak ditemukan.")
        return

    jadwal = user.get("university_schedule", {})
    hari = validasi_hari()
    waktu = validasi_waktu()
    matkul = validasi_mata_kuliah()

    if hari not in jadwal:
        jadwal[hari] = []

    jadwal[hari].append({'waktu': waktu, 'mata_kuliah': matkul})
    user["university_schedule"] = jadwal

    helper.save_user_data(database)
    print("Jadwal berhasil ditambahkan!\n")


def tampilan(username):
    database = helper.load_user_data()
    user = next((user for user in database["users"] if user["username"] == username), None)

    if not user:
        print("User tidak ditemukan.")
        return

    jadwal = user.get("university_schedule", {})
    if not jadwal:
        print("Jadwal kuliah kosong.\n")
        return

    table = PrettyTable()
    table.field_names = ["Hari", "Waktu", "Mata Kuliah"]

    for hari, jadwal_hari in jadwal.items():
        for item in jadwal_hari:
            table.add_row([hari, item['waktu'], item['mata_kuliah']])
        
    print(table)
    print()

def hapusJadwal(username):
    database = helper.load_user_data()
    user = next((user for user in database["users"] if user["username"] == username), None)

    if not user:
        print("User tidak ditemukan.")
        return

    jadwal = user.get("university_schedule", {})
    hari = input("Masukkan hari yang ingin dihapus: ")
    if hari not in jadwal:
        print("Hari tidak ditemukan dalam jadwal.\n")
        return

    tampilan(username)
    try:
        indexHapus = int(input("Masukkan nomor jadwal yang ingin dihapus: ")) - 1
        if 0 <= indexHapus < len(jadwal[hari]):
            jadwal[hari].pop(indexHapus)
            if not jadwal[hari]:
                del jadwal[hari]
            user["university_schedule"] = jadwal
            helper.save_user_data(database)
            print("Jadwal berhasil dihapus.\n")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input tidak valid.")

def editJadwal(username):
    database = helper.load_user_data()
    user = next((user for user in database["users"] if user["username"] == username), None)

    if not user:
        print("User tidak ditemukan.")
        return

    jadwal = user.get("university_schedule", {})
    hari = input("Masukkan hari yang ingin diedit: ")
    if hari not in jadwal:
        print("Hari tidak ditemukan dalam jadwal.\n")
        return

    tampilan(username)
    try:
        indexJadwal = int(input("Masukkan nomor jadwal yang ingin diedit: ")) - 1
        if 0 <= indexJadwal < len(jadwal[hari]):
            waktuBaru = validasi_waktu()
            matkulBaru = validasi_mata_kuliah()
            jadwal[hari][indexJadwal] = {'waktu': waktuBaru, 'mata_kuliah': matkulBaru}
            user["university_schedule"] = jadwal
            helper.save_user_data(database)
            print("Jadwal berhasil diedit!\n")
        else:
            print("Nomor jadwal tidak valid.\n")
    except ValueError:
        print("Input tidak valid.")

def main_jadwal(username):
    while True:
        helper.clear()
        print("1. Tambah Jadwal Kuliah")
        print("2. Tampilkan Jadwal Kuliah")
        print("3. Hapus Jadwal Kuliah")
        print("4. Edit Jadwal Kuliah")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        if pilihan == "1":
            helper.clear()            
            penambahan(username)
            time.sleep(1)            
        elif pilihan == "2":
            helper.clear()
            tampilan(username)
            time.sleep(1)
        elif pilihan == "3":
            helper.clear()
            hapusJadwal(username)
            time.sleep(1)
        elif pilihan == "4":
            helper.clear()
            editJadwal(username)
            time.sleep(1)
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            return
        else:
            print("Invalid. Silakan pilih 1, 2, atau 3.")
