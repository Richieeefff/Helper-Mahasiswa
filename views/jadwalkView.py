import prettytable
from viewmodel import jadwalkViewmodel

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

    while True:
        print("1. Tambah Jadwal Kuliah")
        print("2. Tampilkan Jadwal Kuliah")
        print("3. Hapus Jadwal Kuliah")
        print("4. Edit Jadwal Kuliah")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4/5): ")
        
        if pilihan == "1":
            jadwalkViewmodel.penambahan(jadwal)
        elif pilihan == "2":
            tampilan(jadwal)
        elif pilihan == "3":
            jadwalkViewmodel.hapusJadwal(jadwal)
        elif pilihan == "4":
            jadwalkViewmodel.editJadwal(jadwal)
        elif pilihan == "5":
            print("Terima kasih!, Program selesai.")
            return
        else:
            print("Invalid. Silakan pilih 1, 2, atau 3.")
