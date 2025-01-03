import time
import utils.helper as helper

def load_users():
    return helper.load_user_data()

def save_users(user_data):
    helper.save_user_data(user_data)

def validasi_alpha(prompt):
    return helper.validate_alpha(prompt)

def find_user(username):
    return helper.find_user(username)

def validasi_hari():
    hari_valid = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    
    while True:
        hari = input("Masukkan hari (Senin, Selasa, dst): ").capitalize()
        if hari in hari_valid:
            return hari
        else:
            print("Input tidak valid! Hari harus antara Senin hingga Minggu.")

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

def validasi_waktu(data, hari):
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