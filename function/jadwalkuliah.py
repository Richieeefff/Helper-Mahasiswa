from prettytable import PrettyTable

def validasi_hari():
    hari_valid = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    
    while True:
        hari = input("Masukkan hari (Senin, Selasa, dst): ").capitalize()
        if hari in hari_valid:
            return hari
        else:
            print("Input tidak valid! Hari harus antara Senin hingga Minggu.")

def validasi_waktu():
    while True:
        waktu = input("Masukkan waktu (misal: 08:00 - 10:00): ")
     
        if " - " in waktu:
            start_time, end_time = waktu.split(" - ")
           
            if len(start_time) == 5 and len(end_time) == 5 and start_time[2] == ':' and end_time[2] == ':':
                start_hour, start_minute = start_time.split(":")
                end_hour, end_minute = end_time.split(":")
                
                if start_hour.isdigit() and start_minute.isdigit() and end_hour.isdigit() and end_minute.isdigit():
                    start_hour, start_minute, end_hour, end_minute = map(int, [start_hour, start_minute, end_hour, end_minute])
                    
                    if (0 <= start_hour < 24 and 0 <= start_minute < 60 and 
                        0 <= end_hour < 24 and 0 <= end_minute < 60):
                        return waktu
                    else:
                        print("Waktu tidak valid! Pastikan jam antara 00-23 dan menit antara 00-59.")
                else:
                    print("Jam dan menit harus berupa angka!")
            else:
                print("Format waktu tidak valid! Gunakan format HH:MM - HH:MM.")
        else:
            print("Format waktu tidak valid! Gunakan format HH:MM - HH:MM.")

def validasi_mata_kuliah():
    while True:
        matkul = input("Masukkan nama mata kuliah: ")
        if matkul.isalpha():
            return matkul
        else:
            print("Input tidak valid! Nama mata kuliah hanya boleh berisi huruf.")

def penambahan(jadwal):
    hari = validasi_hari()  
    waktu = validasi_waktu() 
    matkul = validasi_mata_kuliah()
    
    if hari not in jadwal:
        jadwal[hari] = []
    
    jadwal[hari].append({'waktu': waktu, 'mata_kuliah': matkul})
    print("Jadwal berhasil ditambahkan!\n")

def tampilan(jadwal):
    if not jadwal:
        print("Jadwal kuliah kosong.\n")
        return
    
    table = PrettyTable()
    table.field_names = ["Hari","Waktu","Mata Kuliah"]

    for hari, jadwal_hari in jadwal.items():
        for item in jadwal_hari:
            table.add_row([hari, item['waktu'], item['mata_kuliah']])
        
    print(table)
    print()  

def hapusJadwal(jadwal):
    hari = input("Masukkan hari yang ingin dihapus: ")
    if hari not in jadwal:
        print("Hari tidak ditemukan dalam jadwal.\n")
        return
    
    tampilan({hari: jadwal[hari]}) 
    indexHapus = int(input("Masukkan nomor jadwal yang ingin dihapus: ")) - 1
    
    if 0 <= indexHapus < len(jadwal[hari]):
        jadwal[hari].pop(indexHapus)
        print("Jadwal berhasil dihapus")
    else:
        print("Nomor tidak valid")

def editJadwal(jadwal):
    hari = input("Masukkan hari yang ingin diedit: ")
    if hari not in jadwal:
        print("Hari tidak ditemukan dalam jadwal.\n")
        return
    
    tampilan({hari: jadwal[hari]})
    indexJadwal = int(input("Masukkan nomor jadwal yang ingin diedit: ")) - 1
    
    if 0 <= indexJadwal < len(jadwal[hari]):
        waktuBaru = input("Masukkan waktu baru (misal: 08:00 - 10:00): ")
        matkulBaru = input("Masukkan nama mata kuliah baru: ")
        jadwal[hari][indexJadwal] = {'waktu': waktuBaru, 'mata_kuliah': matkulBaru}
        print("Jadwal berhasil diedit!\n")
    else:
        print("Nomor jadwal tidak valid.\n")

def main():
    jadwal = {}  
    
    while True:
        print("1. Tambah Jadwal Kuliah")
        print("2. Tampilkan Jadwal Kuliah")
        print("3. Hapus Jadwal Kuliah")
        print("4. Edit Jadwal Kuliah")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        if pilihan == "1":
            penambahan(jadwal)
        elif pilihan == "2":
            tampilan(jadwal)
        elif pilihan == "3":
            hapusJadwal(jadwal)
        elif pilihan == "4":
            editJadwal(jadwal)
        elif pilihan == "5":
            print("Terima kasih!, Program selesai.")
            return
        else:
            print("Invalid. Silakan pilih 1, 2, atau 3.")
