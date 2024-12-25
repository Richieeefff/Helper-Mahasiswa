import getpass
import time
import utils.helper as helper
from viewmodel.loginViewmodel import register_user, authenticate_user

def display_main_menu():
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
            username = input("Masukkan username: ")
            password = getpass.getpass("Masukkan password: ")
            if authenticate_user(username, password):
                print(f"\nLogin berhasil. Welcome, {username}!")
                time.sleep(1)
                return username
            else:
                print("\nUsername atau Password salah. Silahkan coba lagi.")
                time.sleep(1)
        elif choice == '2':
            helper.clear()
            username = input("Masukkan username: ")
            password = getpass.getpass("Masukkan password baru: ")
            if register_user(username, password):
                print("Berhasil Register.")
                time.sleep(1)
            else:
                print("\nUsername sudah ada! Silakan coba login kembali.")
                time.sleep(1)
        elif choice == '0':
            exit()
        else:
            print("\nInput tidak valid! Silakan coba lagi.")
            time.sleep(1)
