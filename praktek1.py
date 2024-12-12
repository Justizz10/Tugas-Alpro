def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

while True:
    try:
            
        def persegi_panjang():
            panjang = float(input("Masukkan panjang : "))
            lebar = float(input("Masukkan lebar : "))
            luas = luas_persegi_panjang(panjang, lebar)
            print(f"Luas persegi panjang adalah: {luas}")

        persegi_panjang()
        break
    except ValueError:
        print("Tolong masukkan dengan angka")