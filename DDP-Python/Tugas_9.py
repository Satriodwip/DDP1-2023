def profil(nama, alamat, gender, umur, hobi):
    print("nama:", nama)
    print("alamat:", alamat)
    print("gender:", gender)
    print("umur:", umur)
    print("hobi:", hobi)
profil ("Satrio Dwi Pujianto", "Kp Jatijajar RT/08 RW/08", "Male", "20", "Touring")
    

def indikatorkelulusan(nilai):
    if nilai <= 60:
        print("Gagal")
    elif nilai >= 61 and nilai <= 70:
        print("Baik")
    elif nilai >= 71 and nilai <= 80:
        print("Sangat Baik")
    elif nilai >= 81 and nilai <= 100:
        print("Istimewa")
    else :
        print("tidak ditemukan")
nilai = int(input("masukan nilai: "))
indikatorkelulusan(nilai)

def sebut_ganjil(angka):
    for a in range(angka):
        if a % 2 != 0 :
            print(a,end=" ")
bilangan = int(input("masukan angka: "))
sebut_ganjil(bilangan)
