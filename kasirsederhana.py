import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung total belanja, diskon, dan kembalian
def hitung_belanja():
    try:
        harga = float(entry_harga.get())
        jumlah = int(entry_jumlah.get())
        bayar = float(entry_bayar.get())
        
        # Validasi input tidak boleh minus atau nol
        if harga <= 0 or jumlah <= 0 or bayar < 0:
            messagebox.showerror("Error", "Harga, jumlah barang, dan uang bayar harus valid!")
            return
            
        total_harga = harga * jumlah
        
        # Logika percabangan diskon otomatis (if-elif-else)
        if total_harga >= 100000:
            diskon = total_harga * 0.15  # Diskon 15% jika belanja >= 100rb
            info_diskon = "Selamat! Anda mendapat diskon 15% 🎉"
        elif total_harga >= 50000:
            diskon = total_harga * 0.10  # Diskon 10% jika belanja >= 50rb
            info_diskon = "Selamat! Anda mendapat diskon 10% ✨"
        else:
            diskon = 0
            info_diskon = "Belanja di atas 50rb dapat diskon lho!"
            
        total_bayar_akhir = total_harga - diskon
        
        # Cek apakah uang cukup
        if bayar < total_bayar_akhir:
            messagebox.showerror("Uang Kurang", f"Uang pembeli kurang Rp {total_bayar_akhir - bayar:,.0f}!")
            return
            
        kembalian = bayar - total_bayar_akhir
        
        # Tampilkan hasil dalam bentuk struk pop-up
        hasil = (
            f"--- STRUK BELANJA ---\n"
            f"Total Belanja: Rp {total_harga:,.0f}\n"
            f"{info_diskon}\n"
            f"Total Harus Dibayar: Rp {total_bayar_akhir:,.0f}\n"
            f"Uang Bayar: Rp {bayar:,.0f}\n"
            f"Uang Kembalian: Rp {kembalian:,.0f}\n"
            f"---------------------"
        )
        messagebox.showinfo("Hasil Transaksi", hasil)
        
    except ValueError:
        messagebox.showerror("Error", "Mohon masukkan angka yang valid untuk harga, jumlah, dan uang bayar!")

# Fungsi tombol selesai untuk keluar aplikasi
def keluar_aplikasi():
    root.destroy()

# Membuat jendela utama aplikasi desktop
root = tk.Tk()
root.title("Aplikasi Kasir - Toko Sederhana")
root.geometry("440x480")
root.config(bg="#f0f4f8")

# Tombol Selesai (Exit) di pojok kanan atas
tombol_selesai = tk.Button(root, text="❌ Selesai", command=keluar_aplikasi, bg="#ff4d4d", fg="white", font=("Arial", 9, "bold"), padx=5, pady=2)
tombol_selesai.place(x=360, y=10)

# Judul Aplikasi
label_judul = tk.Label(root, text="Kasir Sederhana 🛒", font=("Arial", 16, "bold"), bg="#f0f4f8", fg="#333")
label_judul.pack(pady=20)

label_instruksi = tk.Label(root, text="Hitung total belanja, diskon, dan kembalian secara otomatis!", font=("Arial", 9), bg="#f0f4f8", fg="#555")
label_instruksi.pack(pady=5)

# Input Harga Barang Satuan
tk.Label(root, text="Harga Satuan Barang (Rp):", bg="#f0f4f8", font=("Arial", 10)).pack(pady=3)
entry_harga = tk.Entry(root, font=("Arial", 11), justify="center")
entry_harga.pack(pady=2)

# Input Jumlah Barang
tk.Label(root, text="Jumlah Beli:", bg="#f0f4f8", font=("Arial", 10)).pack(pady=3)
entry_jumlah = tk.Entry(root, font=("Arial", 11), justify="center")
entry_jumlah.pack(pady=2)

# Input Uang Pembayaran
tk.Label(root, text="Uang Pembayaran (Rp):", bg="#f0f4f8", font=("Arial", 10)).pack(pady=3)
entry_bayar = tk.Entry(root, font=("Arial", 11), justify="center")
entry_bayar.pack(pady=2)

# Tombol Hitung / Proses Transaksi
tombol_hitung = tk.Button(root, text="Proses Transaksi 🚀", command=hitung_belanja, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5)
tombol_hitung.pack(pady=15)

# Menjalankan aplikasi
root.mainloop()