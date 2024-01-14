import os
import datetime

def catat_transaksi(nama_file, transaksi):
    with open(nama_file, 'a') as file:
        waktu_sekarang = datetime.datetime.now()
        waktu_format = waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{waktu_format} - {transaksi}\n")
    print("Transaksi berhasil dicatat.")

def tampilkan_catatan(nama_file):
    try:
        with open(nama_file, 'r') as file:
            catatan_keuangan = file.read()
            print("=== Catatan Keuangan ===")
            print(catatan_keuangan)
    except FileNotFoundError:
        print("File catatan keuangan tidak ditemukan. Belum ada transaksi.")

def main():
    nama_file = "catatan_keuangan.txt"

    while True:
        print("\n=== Aplikasi Pencatatan Keuangan ===")
        print("1. Catat Transaksi")
        print("2. Tampilkan Catatan Keuangan")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3): ")

        if pilihan == '1':
            transaksi = input("Masukkan deskripsi transaksi: ")
            catat_transaksi(nama_file, transaksi)
        elif pilihan == '2':
            tampilkan_catatan(nama_file)
        elif pilihan == '3':
            print("Terima kasih, keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
