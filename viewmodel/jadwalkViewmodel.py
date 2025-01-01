from model import jadwalkModel
import utils.helper as helper
from prettytable import PrettyTable
import time

def penambahan(username):
    database = jadwalkModel.load_users()
    for user in database["users"]:
        if user["username"] == username:
            jadwal = user["university_schedule"]
            hari = jadwalkModel.validasi_hari()  
            waktu = jadwalkModel.validasi_waktu(jadwal, hari) 
            matkul = jadwalkModel.validasi_alpha("Masukkan nama mata kuliah: ")
            
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
            jadwalkModel.save_users(database)
            print("Jadwal berhasil ditambahkan!\n")
            time.sleep(1)

def hapusJadwal(username):
    database = jadwalkModel.load_users()
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

                    waktuBaru = jadwalkModel.validasi_waktu(jadwal, hari)
                    matkulBaru = helper.validate_alpha("Masukkan nama mata kuliah: ")

                    for item in edit["jadwal"]:
                        if jadwalkModel.compare_waktu(waktuBaru, item["waktu"]):
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

def tampilan(username):
    user = jadwalkModel.find_user(username)

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