import json
import os
import getpass
import time
import utils.helper as helper

DATA_FILE = 'user_data.json'

def register():
    username = input("Masukkan username: ")
    password = getpass.getpass("Masukkan password baru: ")
    
    user_data = helper.load_user_data()
    
    if username in user_data:
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

def login():
    username = input("Masukkan username: ")
    password = getpass.getpass("Masukkan password: ")
    
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
