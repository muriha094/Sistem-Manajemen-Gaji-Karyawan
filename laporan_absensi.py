class LaporanAbsensi:
    @staticmethod
    def buat_laporan_absensi(absensi):
        """
        Membuat laporan absensi karyawan.
        :param absensi: objek Absensi, berisi data absensi karyawan
        :return: str, laporan absensi lengkap
        """
        laporan = "=== Laporan Absensi ===\n"
        laporan += "ID Karyawan | Hari Hadir | Hari Tidak Hadir | Total Hari\n"
        laporan += "-----------------------------------------------------\n"
        for id_karyawan, jumlah_hari_hadir in absensi.data_absensi.items():
            jumlah_hari_tidak_hadir = absensi.total_hari - jumlah_hari_hadir
            laporan += (
                f"{id_karyawan:<12} | {jumlah_hari_hadir:<10} | {jumlah_hari_tidak_hadir:<15} | {absensi.total_hari}\n"
            )
        return laporan
