# tipe string
#judul_buku = "si_kancil"
#print(judul_buku)

# tipe data integer
#tahun_terbit = 2010
#print(tahun_terbit)

# tipe data float
#penulis = 3.15
#angka_desimal2 = -0,5
#print(angka_desimal2,penulis)

# tipe data boolean
#is_active = True
#not_active = False
#print("laptop anda : ",is_active)

# tipe data list
#daftar_hewan = ["arya","sambo","tito"]
#jumlah_saudara = [3,4,5,6]
#print(daftar_hewan[2])
#print(jumlah_saudara[3])

biodata = {"nama : daffa,nilai: 88,kelas: 1c,absen : tidak ok"
           "nama : chulo,nilai: 90,kelas: 1d,absen : ok"}

nama =str(input("masukan nama :"))
nilai =int(input("masukan nilai :"))
kelas =int(input("masukan kelas :"))
absen =str(input("masukan absen :"))

persyaratan_nilai = 90
persyaratan_absen = 'ok'

if(persyaratan_nilai >= 90)and(absen == persyaratan_absen):
    hasil ='naik kelas'
else:
    hasil ='tidak naik kelas'

print('nama',nama)
print('persyaratan nilai',nilai)
print('persyaratan absen',absen)
print('hasil perssyaratan',hasil)