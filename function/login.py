import re
import getpass
import time
import utils.helper as helper

def register():
    while True:
        username = helper.validate_nospace("Masukkan username: ")
        if len(username) < 3 or len(username) > 20:
            print("Username harus memiliki minimal 3-20 karakter. Coba lagi.")
            time.sleep(1)
            helper.clear()
        else:
            break
    while True:
        password = getpass.getpass("Masukkan password baru: ")
        if len(password) < 6:
            print("Password harus memiliki minimal 6 karakter. Coba lagi.")
            time.sleep(1)
            helper.clear()
        elif not password.strip():
            print("Input tidak boleh kosong! Coba lagi.")
            time.sleep(1)
            helper.clear()
        elif not re.match("^[a-zA-Z0-9!@#$%^&*_ ]+$", password):
            print("Input tidak valid! Password hanya boleh berisi huruf, angka, dan simbol khusus (!@#$%^&*_)")
            time.sleep(1)
            helper.clear()
        else:
            break
    
    user_data = helper.load_user_data()
    
    if any(user["username"] == username for user in user_data["users"]):
        print("\nUsername sudah ada! Silakan coba login kembali.")
        time.sleep(1)
        return
    
    new_user = {
        "username": username,
        "password": password,
        "scheduled_tasks": [],
        "university_schedule": [],
        "exp": 0
    }

    user_data["users"].append(new_user)
    helper.save_user_data(user_data)
    print("Berhasil Register.")
    time.sleep(1)

def login():
    username = helper.validate_nospace("Masukkan username: ")
    while True:
        password = getpass.getpass("Masukkan password: ")
        if not password.strip():
                print("Input tidak boleh kosong! Coba lagi.")
                time.sleep(1)
                helper.clear()
        else:
            break
    
    if username == "admin" and password == "admin":
        return username

    user_data = helper.load_user_data()

    for user in user_data["users"]:
        if  username == user["username"] and password == user["password"]:
            print(f"\nLogin berhasil. Welcome, {username}!")
            time.sleep(1)
            return username
    
    print("\nUsername atau Password salah. Silahkan coba lagi.")
    time.sleep(1)
    return None

def main():

    while True:
        helper.clear()
        print("========================================")
        print("| No |    Masuk Ke Helper Mahasiswa    |")
        print("========================================")
        print("| 1  | Login                           |")
        print("| 2  | Register                        |")
        print("| 0  | Keluar                          |")
        print("========================================")

        choice = input("Pilih dengan angka: ")
        if choice == '1':
            helper.clear()
            result = login()
            if result is not None:
                helper.clear()
                return result
        elif choice == '2':
            helper.clear()
            register()
        elif choice == '0':
            exit()
        else:
            print("\nInput tidak valid! Silakan coba lagi.")
            time.sleep(1)
