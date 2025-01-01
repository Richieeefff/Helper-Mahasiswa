import json
import os
import time
import utils.helper as helper
import sys
import os

DATA_FILE = 'tips_belajar.json'

def load_tips_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return{}

def save_tips_data(tips_data):
    with open(DATA_FILE, 'w') as file:
        json.dump(tips_data, file, indent=4)

def tambah_tips():
    admin = input("Masukkan nama anda: ")
    tips = input("Masukkan Tips: ")
    
    tips_data = load_tips_data()

    for key in tips_data:
        if tips_data[key] == tips:
            return False
    
    tips_data[admin] = tips
    save_tips_data(tips_data)
    return True

def lihat_tips():
    tips = load_tips_data()
    if tips:
        helper.clear()
        for key, value in tips.items():
            print(f"Dari {key.title()}: \"{value.title()}\"")
    else:
        print("Tidak ada tips untuk saat ini")
    time.sleep(3)

def admin_panel():
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
            tambah_tips()
        elif pilihan == '2':
            helper.clear()
            lihat_tips()
        elif pilihan == '0':
            return
        else:
            print("Opsi tidak valid! Silakan coba lagi.")

def main_panel():
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
        lihat_tips()
    elif pilihan == '0':
        return
    else:
        print("\nOpsi tidak valid! Silakan coba lagi.")
        time.sleep(1)

