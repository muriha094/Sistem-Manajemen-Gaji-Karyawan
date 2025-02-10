# 🧾 Sistem Manajemen Gaji Karyawan
Sistem yang saya kembangkan dapat memanajemen gaji seperti menambah data karyawan baru, menginput jabatan, kehadiran, skor target kerja, jam lembur perbulan, dan masih banyak lagi  . Sistem ini memiliki 2 tampilan, yaitu tampilan atasan dan tampilan karyawan. Sistem ini saya kembangkan menggunakan bahasa pyhton.  

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
## 🎯 Fitur-Fitur yang Tersedia 
##### Atasan
1. 📥 Input data karyawan baru seperti nama, jabatan,  kehadiran, Skor target kerja, jumlah jam lembur perbulan
2. 🩹 Dapat menghapus data karyawan
3. 🧾 Melihat laporan gaji, absensi, dan laporan kinerja perbulan. Untuk laporan kinerja perbulan telah diperingkatkan berdasarkan skor total

##### Karyawan
1. 💵 Dapat melihat laporan gaji mereka pada bulan ini
2. 🧾 Melihat peringkat kinerja bulanan mereka

#### Note : 
1. setiap tampilan terdapat menu logout untuk berpindah akun saja dari atasan ke karyawan atau sebaliknya. Dan untuk menu keluar sistem berarti benar-benar keluar sistem dan data akan terhapus, karena data yang diinputkan bersifat sementara.
2. Terdapat potong-potongan gaji, yaitu Asuransi = 2% - gaji pokok, Absensi = apabila melakukan cuti dipotongan gajinya sebanyak hari cuti yang diambil,
   Kinerja = potongan yang terjadi apabila skor total dibawah 60 maka akan dipotongan sebesar Rp 500.000

## 💻 Persyaratan Sistem

- Pyhton versi 3.11.9


## 📁 Struktur 

```sh
├── absensi.py
├── gaji.py
├── jam_kerja.py
├── karyawan.py
├── laporan_absensi.py
├── laporan_gaji.py
├── main.py
└── penilaian_kinerja.py

```


## 🛠️Prosedur Pemakaian Sistem 
Dibawah ini merupakan alur kerja sistem nya
```sh
1.	Login ke sistem, masukkan username dan password untuk admin(admin, admin123)
2.	Pilih menu 1 Tambah Karyawan untuk menambahkan data karyawan baru. Masukkan ID, nama, dan jabatan
3.	Pilih menu 3 Input Absensi dan Penilaian Kinerja untuk menginput kehadiran, skor target kerja, dan jumlah jam lembur selama sebulan.
        Sebelum itu masukkan ID karyawan yang ingin di inputkan datanya terlebih dahulu
4.	Pilih menu 6 Laporan Kinerja Bulanan untuk melihat  laporan kinerja seluruh karyawan yang sudah diperingkatkan.
        Dan untuk melihat laporan yang lainnya juga sama tinggal pilih menu nomor berapa.
5.	Kemudian, kita bisa memilih menu 7 Logout untuk keluar dari tampilan admin dan ganti ke tampilan user.
        Masukkan username dan password untuk user(user, user123). Masukkan salah satu ID karyawan yang telah diinputkan oleh admin tadi
6.	Setelah itu, akan tampil menu-menu yang dapat diakses user, yaitu melihat gaji bulan ini untuk dirinya sendiri
        dan melihat laporan kinerja bulan ini yang telah diperingkatkan.  

```

## Tampilan Sistem
Berikut contoh tampilan dari Sistem Manajemen Gaji Karyawan
##### Atasan
![Picture1](https://github.com/user-attachments/assets/d541fc3f-0ca9-4b46-b101-ca3702ccddc2)
![Picture2](https://github.com/user-attachments/assets/a9d7ad1d-b3dc-49c5-b657-dd407d2b587b)
![Picture3](https://github.com/user-attachments/assets/9fe9cfb2-ec2f-4a49-ab8c-df01c7854330)
![Picture4](https://github.com/user-attachments/assets/cb8d283b-9bb6-4c72-8330-a3274bfd32f5)
![Picture5](https://github.com/user-attachments/assets/d2ae78bb-abc0-406d-9929-7c83eae879f9)
![Picture6](https://github.com/user-attachments/assets/48350c98-c56a-4a52-9939-c0bcf6405a52)
![Picture7](https://github.com/user-attachments/assets/e5695a2e-1ef6-4f3f-a51f-b8a0f8900013)

##### Karyawan
![Picture8](https://github.com/user-attachments/assets/6287221c-8df6-4ebb-a575-0ff4d98bc5cc)
![Picture9](https://github.com/user-attachments/assets/2c75de41-2c88-4919-ac65-d96b979d25f4)
![Picture10](https://github.com/user-attachments/assets/57b2d501-2408-4a9c-b2c3-4ae86aad55e9)
![Picture11](https://github.com/user-attachments/assets/a6af10b0-03be-4f9b-a2f1-eea86cbdb188)







