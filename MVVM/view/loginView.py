import getpass
import time
from viewmodel.loginViewModel import LoginViewModel
import utils.helper as helper

class LoginView:
    def __init__(self):
        self.viewmodel = LoginViewModel()

    def menu(self):
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
                username = self.login()
                if username:
                    return username
            elif choice == '2':
                helper.clear()
                self.register()
            elif choice == '0':
                exit()
            else:
                print("\nInvalid input! Silakan coba lagi.")
                time.sleep(1)

    def register(self):
        username = input("Masukkan username: ")
        password = getpass.getpass("Masukkan password baru: ")
        if self.viewmodel.register_user(username, password):
            print("\nBerhasil Register.")
        else:
            print("\nUsername sudah ada! Silakan coba lagi.")
        time.sleep(1)

    def login(self):
        username = input("Masukkan username: ")
        password = getpass.getpass("Masukkan password: ")
        if username == "admin" and password == "admin":
            print("\nLogin berhasil sebagai admin.")
            time.sleep(1)
            return username
        if self.viewmodel.auth_user(username, password):
            print(f"\nLogin berhasil. Welcome, {username}!")
            time.sleep(1)
            return username
        else:
            print("\nUsername atau Password salah. Silahkan coba lagi.")
            time.sleep(1)
            return None
