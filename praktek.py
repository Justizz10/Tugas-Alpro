stok_barang = 100

def kurangi_stok(jumlah):
    global stok_barang
    if jumlah > stok_barang:
        print(f"Stok tidak cukup! Stok tersedia: {stok_barang}")
        return False
    else:
        stok_barang -= jumlah
        print(f"{jumlah} barang telah terjual. Stok total: {stok_barang}")
        print("Transaksi selesai.")  # Menambahkan pesan transaksi selesai
        return True

def main():
    print("Sistem Manajemen Stok Barang Toko\nStok awal = 100")
    while True:
        try:
            jumlah = int(input("Masukkan jumlah barang yang ingin dikurangi: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0.")
                continue
        except ValueError:
            print("Harap masukkan sebuah angka")
            continue
        
        if kurangi_stok(jumlah):  # Tidak perlu negasi di sini
            lanjut = input("Apakah anda ingin melanjutkan Transaksi? (ya/tidak): ").strip().lower()
            if lanjut == "ya":
                print("Terima kasih telah bertransaksi!")
                break
            elif lanjut == "tidak":
                print("Anda telah membatalkan Transaksi, Silahkan Pulang!")
                break
        

if __name__ == "__main__":
    main()