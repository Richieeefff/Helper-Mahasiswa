import time
from viewmodel.tipsViewmodel import add_tip, get_all_tips
import utils.helper as helper

def display_admin_panel():
    while True:
        helper.clear()
        print("========================================")
        print("| No |          Admin Panel            |")
        print("========================================")
        print("| 1  | Tambah Tips                     |")
        print("| 2  | Lihat Tips                      |")
        print("| 0  | Keluar                          |")
        print("========================================")

        pilihan = input("Pilih opsi (0-2): ")
        if pilihan == '1':
            helper.clear()
            admin = helper.validate_alnum("Masukkan nama anda: ")
            tips = helper.validate_alnum("Masukkan Tips: ")
            if add_tip(admin, tips):
                print("\nTips berhasil ditambahkan!")
            else:
                print("\nTips sudah ada!")
            time.sleep(2)
        elif pilihan == '2':
            helper.clear()
            display_tips()
        elif pilihan == '0':
            return
        else:
            print("\nOpsi tidak valid! Silakan coba lagi.")
            time.sleep(2)

def display_tips():
    tips = get_all_tips()
    if tips:
        helper.clear()
        for key, value in tips.items():
            print(f"Dari {key.title()}: \"{value.title()}\"")
    else:
        print("Tidak ada tips untuk saat ini.")
    time.sleep(3)

def display_main_panel():
    helper.clear()
    print("========================================")
    print("| No |          Tips Belajar           |")
    print("========================================")
    print("| 1  | Lihat Tips                      |")
    print("| 0  | Kembali                         |")
    print("========================================")
    pilihan = input("Pilih opsi (0-1): ")

    if pilihan == '1':
        helper.clear()
        display_tips()
    elif pilihan == '0':
        return
    else:
        print("\nOpsi tidak valid! Silakan coba lagi.")
        time.sleep(1)
