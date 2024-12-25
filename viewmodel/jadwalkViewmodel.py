from model import jadwalkModel
from views import jadwalkView


def penambahan(jadwal):
    hari = jadwalkModel.validasi_hari()  
    waktu = jadwalkModel.validasi_waktu() 
    matkul = jadwalkModel.validasi_mata_kuliah()
    
    if hari not in jadwal:
        jadwal[hari] = []
    
    jadwal[hari].append({'waktu': waktu, 'mata_kuliah': matkul})
    print("Jadwal berhasil ditambahkan!\n")

def hapusJadwal(jadwal):
    hari = input("Masukkan hari yang ingin dihapus: ")
    if hari not in jadwal:
        print("Hari tidak ditemukan dalam jadwal.\n")
        return
    
    jadwalkView.tampilan({hari: jadwal[hari]}) 
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
    
    jadwalkView.tampilan({hari: jadwal[hari]})
    indexJadwal = int(input("Masukkan nomor jadwal yang ingin diedit: ")) - 1
    
    if 0 <= indexJadwal < len(jadwal[hari]):
        waktuBaru = input("Masukkan waktu baru (misal: 08:00 - 10:00): ")
        matkulBaru = input("Masukkan nama mata kuliah baru: ")
        jadwal[hari][indexJadwal] = {'waktu': waktuBaru, 'mata_kuliah': matkulBaru}
        print("Jadwal berhasil diedit!\n")
    else:
        print("Nomor jadwal tidak valid.\n")
