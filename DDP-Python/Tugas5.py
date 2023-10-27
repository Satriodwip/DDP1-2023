kendaraan = ["Vario 160","Motor","160cc","Hitam","roda 2,"]
print(kendaraan)

#dari program yang di atas tambahkan: di akhir tambahkan [harga kendaraan dan jumlah roda] di sisipkan setelah nama kendaraan [merk kendaraan dan jenis kendaraan]

kendaraan.append("Rp26.000.000")
kendaraan.append("Matic")
kendaraan.insert(2,"Honda")
print("Kendaraan ini saya gunakan untuk kepeerluan sehari-hari")
print(kendaraan)

#Menghitung luas bangun datar

menghitung = input("PILIH OPERASI: \n 1. hitung luas persegi \n 2. hitung luas lingkaran \n 3.2 hitung luas segitiga \n pilihan: ")
match menghitung:
    case "1":
        sisi= int (input("masukan nilai sisi: "))
        luas = sisi*sisi
        print(luas)
    case "2":
        jari_jari= int (input("masukan nilai jari-jari: "))
        luas = 3.14* jari_jari*jari_jari
        print(luas)
    case "3":
        alas = int (input("masukan nilai alas: "))
        tinggi = int (input("masukan nilai tinggi: "))
        luas = 0.5*alas*tinggi
        print(luas)
    case _:
        print("salah pilih")
        
        
        
    