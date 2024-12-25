


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
