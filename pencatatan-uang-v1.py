import pandas as pd
from tkinter import *
from datetime import datetime

class PencatatanUangApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikasi Pencatatan Uang")

        # Inisialisasi DataFrame
        self.df = pd.DataFrame(columns=["nama_pencatatan", "jumlah_uang", "tanggal_pencatatan", "waktu_pencatatan"])

        # Label dan Entry untuk input
        Label(master, text="Nama Pencatatan:").grid(row=0, column=0)
        Label(master, text="Jumlah Uang:").grid(row=1, column=0)
        Label(master, text="Tanggal Pencatatan:").grid(row=2, column=0)

        self.nama_entry = Entry(master)
        self.nama_entry.grid(row=0, column=1)

        self.jumlah_entry = Entry(master)
        self.jumlah_entry.grid(row=1, column=1)

        self.tanggal_entry = Entry(master)
        self.tanggal_entry.grid(row=2, column=1)

        # Tombol untuk menyimpan data
        Button(master, text="Simpan", command=self.simpan_data).grid(row=3, column=0, columnspan=2)

    def simpan_data(self):
        nama_pencatatan = self.nama_entry.get()
        jumlah_uang = float(self.jumlah_entry.get())
        tanggal_pencatatan = self.tanggal_entry.get()
        waktu_pencatatan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Menambahkan data ke DataFrame
        new_data = pd.DataFrame([[nama_pencatatan, jumlah_uang, tanggal_pencatatan, waktu_pencatatan]],
                                columns=["nama_pencatatan", "jumlah_uang", "tanggal_pencatatan", "waktu_pencatatan"])
        self.df = pd.concat([self.df, new_data], ignore_index=True)

        # Menyimpan DataFrame ke file Excel
        self.df.to_excel("pencatatan_uang.xlsx", index=False)

        # Membersihkan input setelah menyimpan
        self.nama_entry.delete(0, END)
        self.jumlah_entry.delete(0, END)
        self.tanggal_entry.delete(0, END)

        print("Data berhasil disimpan.")

if __name__ == "__main__":
    root = Tk()
    app = PencatatanUangApp(root)
    root.mainloop()
