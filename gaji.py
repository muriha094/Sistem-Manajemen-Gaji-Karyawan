class Gaji:
    def __init__(self):
        # Menyimpan data gaji karyawan dalam format {id_karyawan: gaji_pokok}
        self.data_gaji = {}

    def tambah_karyawan(self, id_karyawan, gaji_pokok):
        """
        Menambahkan karyawan baru beserta gaji pokoknya.
        :param id_karyawan: str, ID karyawan
        :param gaji_pokok: int, jumlah gaji pokok
        """
        if id_karyawan in self.data_gaji:
            raise ValueError("ID Karyawan sudah ada dalam sistem.")
        self.data_gaji[id_karyawan] = gaji_pokok

    def hapus_karyawan(self, id_karyawan):
        """
        Menghapus data karyawan berdasarkan ID.
        :param id_karyawan: str, ID karyawan
        """
        if id_karyawan not in self.data_gaji:
            raise ValueError("ID Karyawan tidak ditemukan.")
        del self.data_gaji[id_karyawan]

    def hitung_gaji_bulanan(self, id_karyawan, penilaian_kinerja):
        """
        Menghitung gaji bulanan karyawan termasuk bonus, potongan absensi, dan asuransi.
        :param id_karyawan: str, ID karyawan
        :param penilaian_kinerja: PenilaianKinerja, objek kelas PenilaianKinerja
        :return: int, total gaji bulanan setelah semua potongan dan bonus
        """
        if id_karyawan not in self.data_gaji:
            raise ValueError("ID Karyawan tidak ditemukan.")

        gaji_pokok = self.data_gaji[id_karyawan]
        bonus = penilaian_kinerja.hitung_bonus(id_karyawan)  # Menghitung bonus berdasarkan penilaian kinerja
        potongan_absensi = penilaian_kinerja.hitung_potongan(id_karyawan)  # Menghitung potongan absensi
        asuransi = gaji_pokok * 0.02  # Potongan untuk asuransi (5% dari gaji pokok)

        total_gaji = gaji_pokok + bonus - potongan_absensi - asuransi
        return total_gaji

    def tampilkan_gaji(self, id_karyawan):
        """
        Menampilkan gaji pokok karyawan berdasarkan ID.
        :param id_karyawan: str, ID karyawan
        """
        if id_karyawan not in self.data_gaji:
            raise ValueError("ID Karyawan tidak ditemukan.")
        print(f"Gaji Pokok untuk ID Karyawan {id_karyawan}: Rp{self.data_gaji[id_karyawan]:,}")
