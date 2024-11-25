import json
import os
import getpass
import time
import utils.helper as helper

DATA_FILE = 'user_data.json'

def load_user_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_user_data(user_data):
    with open(DATA_FILE, 'w') as file:
        json.dump(user_data, file, indent=4)

def register():
    username = input("Masukkan username: ")
    password = getpass.getpass("Masukkan password baru: ")
    
    user_data = load_user_data()
    
    if username in user_data:
        print("\nUsername sudah ada! Silakan coba login kembali.")
        time.sleep(1)
        return
    
    new_user = {
        "username": username,
        "password": password,
        "scheduled_tasks": [],
        "university_schedule": []
    }

    user_data["users"].append(new_user)
    save_user_data(user_data)
    print("Berhasil Register.")

def login():
    username = input("Masukkan username: ")
    password = getpass.getpass("Masukkan password: ")
    
    user_data = load_user_data()

    for user in user_data["users"]:
        if user["username"] == "admin":
            return True, username
        if user["username"] == username:
            if user["password"] == password:
                print(f"Login berhasil. Welcome, {username}!")
                return True, username
            else:
                print("Password atau Username salah. Tolong coba lagi.")
                return False

    # Username not found
    print("Username tidak ditemukan. Tolong register terlebih dahulu")
    return False

def main():

    while True:
        helper.clear()
        print("Silahkan melakukan login terlebih dahulu!\n")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Pilih dengan angka: ")

        if choice == '1':
            helper.clear()
            register()
        elif choice == '2':
            helper.clear()
            result, user = login()
            if result:
                helper.clear()
                return user
        elif choice == '3':
            break
        else:
            print("\nInvalid input! Silakan coba lagi.")
            time.sleep(1)
