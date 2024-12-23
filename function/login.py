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
    
    user_data = helper.load_user_data()

    if username == "admin" and password == "admin":
        return username

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
            result = login()
            if result is not None:
                helper.clear()
                return result
        elif choice == '3':
            break
        else:
            print("\nInvalid input! Silakan coba lagi.")
            time.sleep(1)
