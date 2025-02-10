class Absensi:
    def __init__(self):
        self.data_absensi = {}
        self.total_hari = 30

    def tambah_absensi(self, id_karyawan, jumlah_hari_hadir):
        if jumlah_hari_hadir < 0 or jumlah_hari_hadir > self.total_hari:
            raise ValueError("Jumlah hari hadir tidak valid.")
        self.data_absensi[id_karyawan] = jumlah_hari_hadir

    def hitung_potongan(self, id_karyawan, jabatan):
        if id_karyawan not in self.data_absensi:
            raise ValueError("Data absensi karyawan tidak ditemukan.")

        potongan_per_hari = {
            'Direktur': 333333.3,
            'Manajer': 266666.67,
            'Supervisor': 166666.67,
            'Staf Administrasi': 133333.3,
            'Desain Grafis': 100000
        }

        jumlah_hari_hadir = self.data_absensi[id_karyawan]
        jumlah_tidak_hadir = self.total_hari - jumlah_hari_hadir

        if jabatan not in potongan_per_hari:
            raise ValueError("Jabatan tidak valid.")

        return jumlah_tidak_hadir * potongan_per_hari[jabatan]

    def tampilkan_laporan(self):
        print("========= Laporan Absensi ========")
        for id_karyawan, jumlah_hari_hadir in self.data_absensi.items():
            print(f"ID Karyawan: {id_karyawan}, Hari Hadir: {jumlah_hari_hadir}/{self.total_hari}")
