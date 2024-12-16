from viewmodel.tugasViewModel import TugasViewModel
import utils.helper as helper
from datetime import datetime
import time

class TugasView:
    def __init__(self, username):
        self.viewmodel = TugasViewModel(username)
        self.username = username
    
    def display(self):
        while True:
            helper.clear()
            print("========================================")
            print("| No |          Menu Tugas             |")
            print("========================================")
            print("| 1  | Menambahkan Tugas               |")
            print("| 2  | Melihat Tugas                   |")
            print("| 3  | Selesaikan Tugas                |")
            print("| 0  | Keluar                          |")
            print("========================================")
            
            pilihan = input("Pilih opsi (0-3): ")
            if pilihan == '1':
                date, matkul, judul, desc, diff, dl = self.get_tugas_input()
                if self.viewmodel.add_tugas(date, matkul, judul, desc, diff, dl):
                    print("Tugas berhasil ditambahkan")
                else:
                    print("Terdapat kesalahan!")
                time.sleep(3)
            elif pilihan == '2':
                self.display_tugas()
                time.sleep(5)
            elif pilihan == '3':
                self.display_tugas()
                rm = int(input("Masukkan nomor tugas yang ingin di hapus: "))
                result = self.viewmodel.selesai_tugas(rm)
                if result:
                    print(result)
                    time.sleep(3)
                    helper.clear()
                    self.display_tugas()
                    time.sleep(5)
                else:
                    print("ID tugas salah! Silahkan coba lagi.")
                    time.sleep(3)
                
            elif pilihan == '0':
                return
            else:
                print("Opsi tidak valid! Silakan coba lagi.")
    
    def get_valid_date(self, prompt):
        """
        Prompt the user for a valid date in the format DD-MM-YYYY.
        """
        while True:
            date_input = input(prompt)
            try:
                datetime.strptime(date_input, "%d-%m-%Y")
                return date_input
            except ValueError:
                print("Format tanggal tidak valid. Harap masukkan dalam format DD-MM-YYYY.")

    def get_tugas_input(self):
        helper.clear()

        date = self.get_valid_date("Masukkan tanggal (DD-MM-YYYY):")
        matkul = input("Masukkan nama mata kuliah: ")
        judul = input("Masukkan judul tugas: ")
        desc = input("Masukkan deskripsi  tugas: ")
        while True:
            print("Pilih tingkat kesulitan tugas:")
            print("1. Mudah")
            print("2. Sedang:")
            print("3. Sulit")
            diffChoice = input("Piling opsi (1-3): ")
            if diffChoice == '1':
                diff = "mudah"
                break
            elif diffChoice == '2':
                diff = "sedang"
                break
            elif diffChoice == '3':
                diff = "sulit"
                break
            else:
                print("Opsi tidak valid! Silakan coba lagi.\n")
                time.sleep(3)
        dl = self.get_valid_date("\nMasukkan tanggal tenggat tugas (DD-MM-YYYY):")

        return date, matkul, judul, desc, diff, dl
    
    def display_tugas(self):
        """Display tasks nicely."""
        helper.clear()
        result = self.viewmodel.get_tugas()

        if "error" in result:
            print(result["error"])
            return
        if "message" in result:
            print(result["message"])
            return

        tasks = result["tasks"]
        print(f"Tugas pending {self.username}:")
        print("=" * 50)
        for i, task in enumerate(tasks, 1):
            print(f"Tugas {i}:")
            print(f"  - Date: {task['tanggal']}")
            print(f"  - Course: {task['mata_kuliah']}")
            print(f"  - Title: {task['judul']}")
            print(f"  - Description: {task['deskripsi']}")
            print(f"  - Difficulty: {task['tingkat_kesulitan']}")
            print(f"  - Deadline: {task['tenggat']}")
            print(f"  - Status: {task['status']}")
            print("=" * 50)