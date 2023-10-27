# Meminta pengguna memasukkan usia
nama = "udin petot"
usia = 45
# Menentukan kategori usia
if usia < 18:
    kategori = "Anak-anak"
elif 18 <= usia <= 65:
    kategori = "Dewasa"
else:
    kategori = "Lanjut Usia"

# Menampilkan kategori usia
print ("nama anda \t:",nama,"\nusia anda\t:",usia,"\nketegori \t:",kategori)
print()

# Menentukan Nilai yang lebih besar dan Memakai Keterangan
x = 30
y = 30

if(x > y):
    grade = "x lebih besar dari y"
elif(y > x):
    grade = "y lebih besar dari x"
else:
    grade = "x dan y memilki nilai yang sama"
print(grade)
