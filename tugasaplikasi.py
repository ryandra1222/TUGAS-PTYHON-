data_mahasiswa = {}

def display_menu():
    print("\nMenu:")
    print("1. [1] Lihat Data Mahasiswa dan NIM")
    print("2. [2] Tambah Data")
    print("3. [3] Edit Data")
    print("4. [4] Hapus Data")
    print("5. [0] EXIT")

def display_data():
    if not data_mahasiswa:
        print("Data belum ada.")
    else:
        print("\nData Mahasiswa:")
        for nim, nama in data_mahasiswa.items():
            print(f" {nim} | |  {nama}")

def tambah_data():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    data_mahasiswa[nim] = nama
    print("Data mahasiswa berhasil ditambahkan.")

def edit_data():
    if not data_mahasiswa:
        print("Data belum ada.")
        return
    
    nim = input("Masukkan NIM mahasiswa yang ingin diubah: ")
    if nim in data_mahasiswa:
        nama_baru = input("Masukkan Nama Baru: ")
        data_mahasiswa[nim] = nama_baru
        print("Data mahasiswa berhasil diubah.")
    else:
        print("NIM tidak ditemukan.")

def hapus_data():
    if not data_mahasiswa:
        print("Data belum ada.")
        return
    
    nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
    if nim in data_mahasiswa:
        del data_mahasiswa[nim]
        print("Data mahasiswa berhasil dihapus.")
    else:
        print("NIM tidak ditemukan.")

def main():
    while True:
        display_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            display_data()
        elif pilihan == '2':
            tambah_data()
        elif pilihan == '3':
            edit_data()
        elif pilihan == '4':
            hapus_data()
        elif pilihan == '0':
            print("Terima kasih telah menggunakan Aplikasi  ini.")
            break
        else:
            print("Pilihan tidak valid, silakan pilih lagi.")

main()  # Memanggil fungsi main() langsung
