from function import login

def penambahan(username):
    
    tanggal = input("Masukkan tanggal (YYYY-MM-DD):")
    matkul = input("Masukkan nama mata kuliah: ")
    judul = input("Masukkan judul tugas: ")
    deskripsi = input("Masukkan deskripsi  tugas: ")
    kesulitan = input("Masukkan Tingkat kesulitan (Mudah/Sedang/Sulit): ")
    tenggat = input("Masukkan tanggal tenggat tugas (YYYY-MM-DD):")

    
    database = login.load_user_data()
    for user in database["users"]:
        if user["username"] == username:
            user["scheduled_tasks"].append({
                                    'tanggal': tanggal,
                                    'mata_kuliah': matkul, 
                                    'judul': judul,
                                    'deskripsi': deskripsi,
                                    'tingkat_kesulitan': kesulitan,
                                    'tenggat': tenggat,
                                    'status':'Belum Selesai'
                                    })
            login.save_user_data(database)
            print("Tugas berhasil ditambahkan!\n")
            return
    print(f"User {username} not found.")


def tampilan(tugas):

    data = login.load_user_data()

    for user in data["users"]:
        print(f"Username: {user['username']}\n")
        print("Scheduled Tasks:")
        for task in user["scheduled_tasks"]:
            print(f"- Tanggal: {task['tanggal']}")
            print(f"  Mata Kuliah: {task['mata_kuliah']}")
            print(f"  Judul: {task['judul']}")
            print(f"  Deskripsi: {task['deskripsi']}")
            print(f"  Tingkat Kesulitan: {task['tingkat_kesulitan']}")
            print(f"  Tenggat: {task['tenggat']}")
            print(f"  Status: {task['status']}\n")
        print("-" * 50)

    if not data:
        print("Cie lagi gak ada tugas.\n")
        return

    

def selesaikanTugas(tugas):
    tanggal = input("Masukkan tanggal tugas yang ingin diselesaikan (YYYY-MM-DD): ")
    if tanggal not in tugas:
        print("Tidak ada tugas pada tanggal tersebut.\n")
        return
    
    print("Tugas yang tersedia untuk tanggal tersebut:")
    for i, isiTugas in enumerate(tugas[tanggal]):
        print(f"{i + 1}. {isiTugas['judul']} - Status: {isiTugas['status']}")

    pilihan = int(input("Pilih nomor tugas yang ingin diselesaikan: ")) - 1
    if 0 <= pilihan < len(tugas[tanggal]):
        tugasPilihan = tugas[tanggal][pilihan]
        print(f"Status tugas '{tugasPilihan['judul']}' saat ini: {tugasPilihan['status']}")
        
        statusBaru = input("Apakah tugas ini sudah selesai? (ya/tidak): ").strip().lower()
        if statusBaru == 'ya':
            tugasPilihan['status'] = 'Selesai'
            print("Status berhasil diubah menjadi 'Selesai'!\n")
        elif statusBaru == 'tidak':
            tugasPilihan['status'] = 'Belum Selesai'
            print("Status berhasil diubah menjadi 'Belum Selesai'!\n")
        else:
            print("Input tidak valid. Masukkan 'ya' atau 'tidak'.\n")
    else:
        print("Pilihan tidak valid.\n")

def hapusTugas(username):
    tanggal = input("Masukkan tanggal tugas yang ingin dihapus (YYYY-MM-DD): ")
    judul = input("Masukkan judul tugas yang ingin dihapus: ")

    database = login.load_user_data()
    for user in database["users"]:
        if user["username"] == username:
            for tugas in user["scheduled_tasks"]:
                if tugas["tanggal"] == tanggal and tugas["judul"] == judul:
                    user["scheduled_tasks"].remove(tugas)
                    login.save_user_data(database)
                    print(f"Tugas '{judul}' pada tanggal {tanggal} berhasil dihapus!\n")
                    return
            print("Tugas tidak ditemukan.")
            return
    print(f"User {username} tidak ditemukan.")

def main_tugas(username):
    tugas = {}
    
    while True:
        print("1. Menambah Tugas")
        print("2. Menampilkan Tugas")
        print("3. Selesaikan Tugas")
        print("4. Menghapus Tugas")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        if pilihan == "1":
            penambahan(username)
        elif pilihan == "2":
            tampilan(tugas)
        elif pilihan == "3":
            selesaikanTugas(tugas)
        elif pilihan == "4":
            hapusTugas(username)
        elif pilihan == "5":
            print("Terima kasih!, Program selesai.")
            return
        else:
            print("Invalid. Silakan pilih 1, 2, 3, 4 atau 5.")
