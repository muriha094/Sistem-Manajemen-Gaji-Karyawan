class Karyawan:
    JABATAN = {
        'a': ('Direktur', 10000000),
        'b': ('Manajer', 8000000),
        'c': ('Supervisor', 5000000),
        'd': ('Staf Administrasi', 4000000),
        'e': ('Desain Grafis', 3000000)
    }

    def __init__(self, id_karyawan, nama, pilihan_jabatan):
        if pilihan_jabatan not in self.JABATAN:
            raise ValueError("Pilihan jabatan tidak valid")
        self.id_karyawan = id_karyawan
        self.nama = nama
        self.jabatan, self.gaji_pokok = self.JABATAN[pilihan_jabatan]

    def tampilkan_info(self):
        return f"ID: {self.id_karyawan}, Nama: {self.nama}, Jabatan: {self.jabatan}, Gaji Pokok: {self.gaji_pokok}"


class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = {}

    def tambah_karyawan(self, id_karyawan, nama, pilihan_jabatan):
        if id_karyawan in self.daftar_karyawan:
            print("Karyawan dengan ID ini sudah ada.")
            return
        karyawan_baru = Karyawan(id_karyawan, nama, pilihan_jabatan)
        self.daftar_karyawan[id_karyawan] = karyawan_baru
        print(f"Karyawan {nama} dengan ID {id_karyawan} berhasil ditambahkan.")

    def hapus_karyawan(self, id_karyawan):
        if id_karyawan in self.daftar_karyawan:
            del self.daftar_karyawan[id_karyawan]
            print(f"Karyawan dengan ID {id_karyawan} berhasil dihapus.")
        else:
            print("Karyawan tidak ditemukan.")

    def ambil_karyawan(self, id_karyawan):
        if id_karyawan in self.daftar_karyawan:
            return self.daftar_karyawan[id_karyawan]
        else:
            raise ValueError(f"Karyawan dengan ID {id_karyawan} tidak ditemukan.")
