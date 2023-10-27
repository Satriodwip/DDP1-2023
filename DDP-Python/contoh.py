#deklasri dan inisialisasi variabel
pelanggan = "asep galon"
total_belanja = 60000

#sturuktur kendali if
if(total_belanja > 300000):
    keterangan = "selamat mendapat hadiah"
else:
    keterangan = "terima kasih"
    
#cetak data
print("pelanggan", pelanggan,"\ttotal belanja anda Rp.",total_belanja,"\t",keterangan)
print()
#siswa dinyatakan lulus minimal 75 nilainya
nama = "juned"
matpel = "Matkom"
nilai = 67.75
#ternary
if (nilai >= 75 ):
    keterangan ="lulus"
    
else : 
    keterangan ="gagal"

#cetak

print ("nama siswa \t:",nama,"\nMata Pelajaran \t:",matpel,"\nNilai \t\t:",nilai,"\nKeterangan \t:",keterangan)


print()
#siswa dinyatakan lulus minimal 75 nilainya
nama = "juned"
matpel = "Matkom"
nilai = 77.75
#ternary
if (nilai >= 90 and nilai <=100):
    grade ="A"
elif  (nilai >= 85 and nilai < 90):
    grade ="B"
elif (nilai >= 70 and nilai < 80):
    grade ="C"
elif (nilai >= 65 and nilai < 70):
    grade ="D"
else :
    grade ="E"
    
print ("nama siswa \t:",nama,"\nMata Pelajaran \t:",matpel,"\nNilai \t\t:",nilai,"\ngrade \t:",grade)


