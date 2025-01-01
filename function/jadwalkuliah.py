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

def waktu_input(data, hari):
    while True:
        try:
            waktu = input("Masukkan waktu (misal: 08:00-10:00): ").strip()
            if "-" in waktu:
                start, end = waktu.split("-")
                start_time = helper.validate_time(start)
                end_time = helper.validate_time(end)
                if start_time and end_time:
                    if start_time >= end_time:
                        print("Waktu selesai tidak bisa kurang dari waktu awal! Coba lagi.")
                        time.sleep(1)
                        helper.clear()
                    else:
                        conflict = False # Cek apabila ada konflik dengan jadwal lain di hari yang sama

                        for day in data:
                            if day["hari"] == hari: 
                                for item in day["jadwal"]:
                                    if compare_waktu(waktu, item["waktu"]):
                                        print(f"Jadwal {waktu} bertabrakan dengan jadwal {item['waktu']} di hari {hari}.")
                                        time.sleep(1)
                                        helper.clear()
                                        conflict = True
                                        break 
                            if conflict: 
                                break
                        if not conflict:
                            return waktu
                else:
                    print("Format waktu tidak valid! Gunakan format HH:MM-HH:MM.")
                    time.sleep(1)
                    helper.clear()
            else:
                print("Format waktu tidak valid! Gunakan format HH:MM-HH:MM.")
                time.sleep(1)
        except ValueError:
            print("Format waktu tidak valid! Gunakan format HH:MM-HH:MM.")
            time.sleep(1)
            helper.clear()

def compare_waktu(waktu1, waktu2): # Membandingkan 2 jadwal waktu apakah conflict atau tidak
    start_str, end_str = waktu1.split("-")
    startnew_str, endnew_str = waktu2.split("-")
    start = helper.validate_time(start_str)
    end = helper.validate_time(end_str)
    start_new = helper.validate_time(startnew_str)
    end_new = helper.validate_time(endnew_str)

    if start < end_new and start_new < end:
        return True
    return False

def penambahan(username):
    database = helper.load_user_data()
    for user in database["users"]:
        if user["username"] == username:
            jadwal = user.get("university_schedule", [])
            hari = validasi_hari()
            waktu = waktu_input(jadwal, hari)
            matkul = helper.validate_alpha("Masukkan nama mata kuliah: ")

            for day in jadwal:
                if day["hari"] == hari:
                    day["jadwal"].append({"waktu": waktu, "mata_kuliah": matkul}) 
                    break # Jika hari sudah ada di database break dari loop sehingga bagian "else" tidak akan di run
            else: # Jika tidak ditemukan maka tambah hari baru
                jadwal.append({
                "hari": hari,
                "jadwal": [{"waktu": waktu, "mata_kuliah": matkul}]
            })   

            user["university_schedule"] = jadwal
            helper.save_user_data(database)
            print("Jadwal berhasil ditambahkan!\n")
            time.sleep(1)
            return
    else: 
        print("User tidak ditemukan.")

def tampilan(username):
    user = helper.find_user(username)

    if not user:
        print("User tidak ditemukan.")
        return

    jadwal = user.get("university_schedule", [])
    if not jadwal:
        print("Jadwal kuliah kosong.\n")
        return

    table = PrettyTable()
    table.field_names = ["Hari", "Waktu", "Mata Kuliah"]

    for day in jadwal:
        hari = day["hari"]
        for item in day["jadwal"]:
            table.add_row([hari, item["waktu"], item["mata_kuliah"]])
        
    print(table)

def hapusJadwal(username):
    database = helper.load_user_data()
    for user in database["users"]:
        if user["username"] == username:
            jadwal = user.get("university_schedule", [])
            hari = input("Masukkan hari yang ingin dihapus: ").capitalize()

            delete = next((day for day in jadwal if day["hari"] == hari), None)
            
            if not delete:
                print("Hari tidak ditemukan dalam jadwal.\n")
                return

            tampilan(username) 
            try:
                print(f"Jadwal pada hari {hari}:")
                for idx, item in enumerate(delete["jadwal"], 1):
                    print(f"{idx}. Waktu: {item['waktu']} - Mata Kuliah: {item['mata_kuliah']}")

                indexHapus = int(input("Masukkan nomor jadwal yang ingin dihapus: ")) - 1

                if 0 <= indexHapus < len(delete["jadwal"]):
                    delete["jadwal"].pop(indexHapus) 
                    if not delete["jadwal"]:  
                        jadwal.remove(delete)

                    user["university_schedule"] = jadwal
                    helper.save_user_data(database) 
                    print("Jadwal berhasil dihapus.\n")
                    time.sleep(1)
                    return
                else:
                    print("Nomor tidak valid.")
                    time.sleep(1)
            except ValueError:
                print("Input tidak valid.")
                time.sleep(1)
    else:
        print("User tidak ditemukan.")
        time.sleep(1)
        return 

def editJadwal(username):
    database = helper.load_user_data()
    for user in database["users"]:
        if user["username"] == username:
            jadwal = user.get("university_schedule", [])
            hari = input("Masukkan hari yang ingin diedit: ").capitalize()

            edit = next((day for day in jadwal if day["hari"] == hari), None)

            if not edit:
                print("Hari tidak ditemukan dalam jadwal.\n")
                return

            tampilan(username)
            try:
                print(f"Jadwal pada hari {hari}:")
                for idx, item in enumerate(edit["jadwal"], 1):
                    print(f"{idx}. Waktu: {item['waktu']} - Mata Kuliah: {item['mata_kuliah']}")

                indexJadwal = int(input("Masukkan nomor jadwal yang ingin diedit: ")) - 1

                if 0 <= indexJadwal < len(edit["jadwal"]):
                    old_schedule = edit["jadwal"][indexJadwal]
                    edit["jadwal"].pop(indexJadwal) # Hapus jadwal yang ingin diedit untuk menghindari adanya conflict dengan waktu sebelumnya

                    waktuBaru = waktu_input(jadwal, hari)
                    matkulBaru = helper.validate_alpha("Masukkan nama mata kuliah: ")

                    for item in edit["jadwal"]:
                        if compare_waktu(waktuBaru, item["waktu"]):
                            print(f"Jadwal {waktuBaru} bertabrakan dengan jadwal {item['waktu']} di hari {hari}.")
                            time.sleep(1)
                            break
                    else: 
                        edit["jadwal"].append({'waktu': waktuBaru, 'mata_kuliah': matkulBaru})
                        user["university_schedule"] = jadwal
                        helper.save_user_data(database)
                        print("Jadwal berhasil diedit!\n")
                        time.sleep(1)
                        return
                    if item in edit["jadwal"]:
                        edit["jadwal"].insert(indexJadwal, old_schedule)
                        return
                else:
                    print("Nomor jadwal tidak valid.\n")
                    time.sleep(1)
            except ValueError:
                print("Input tidak valid.")
                time.sleep(1)
    else:
        print("User tidak ditemukan.")
        time.sleep(1)
        return

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
        elif pilihan == "0":
            return
        else:
            print("Opsi tidak valid! Silakan coba lagi.")
