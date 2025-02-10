

class PenilaianKinerja:
    def __init__(self):
        # Data penilaian disimpan dalam format: {id_karyawan: {'kehadiran': nilai, 'target': nilai, 'lembur': nilai, 'skor_total': nilai}}
        self.data_penilaian = {}

    def beri_penilaian(self, id_karyawan, kehadiran, target, lembur=0):
        """
        Memberikan penilaian kepada karyawan berdasarkan kehadiran, pencapaian target, dan lembur.
        :param id_karyawan: str, ID karyawan
        :param kehadiran: int, nilai kehadiran (0-30 hari)
        :param target: int, nilai pencapaian target (0-100)
        :param lembur: int, nilai lembur (0-100)
        """
        # Mengkonversi kehadiran ke dalam skor 0 - 100, jika kehadiran 30 maka 100
        kehadiran_poin = 100 if kehadiran == 30 else (kehadiran / 30) * 100

        # Menghitung skor total berdasarkan bobot
        skor_total = (kehadiran_poin * 0.4) + (target * 0.5) + (lembur * 0.1)

        # Menyimpan data penilaian karyawan
        self.data_penilaian[id_karyawan] = {
            'kehadiran': kehadiran_poin,
            'target': target,
            'lembur': lembur,
            'skor_total': skor_total
        }

    def hitung_bonus(self, id_karyawan):
        """
        Menghitung bonus berdasarkan skor total kinerja.
        :param id_karyawan: str, ID karyawan
        :return: float, persen bonus yang diberikan (dalam bentuk desimal)
        """
        if id_karyawan not in self.data_penilaian:
            return 0  # Tidak ada penilaian, tidak ada bonus

        skor_total = self.data_penilaian[id_karyawan]['skor_total']
        if skor_total >= 90:
            return 0.2  # Bonus 20% dari gaji pokok
        elif skor_total >= 75:
            return 0.1  # Bonus 10% dari gaji pokok
        elif skor_total >= 60:
            return 0.05  # Bonus 5% dari gaji pokok
        else:
            return 0  # Tidak ada bonus untuk kinerja di bawah 60

    def hitung_potongan(self, id_karyawan):
        """
        Menghitung potongan berdasarkan skor total kinerja.
        :param id_karyawan: str, ID karyawan
        :return: int, jumlah potongan berdasarkan kinerja
        """
        if id_karyawan not in self.data_penilaian:
            return 0  # Tidak ada penilaian, tidak ada potongan

        skor_total = self.data_penilaian[id_karyawan]['skor_total']
        if skor_total < 60:
            return 500000  # Potongan sebesar 500.000 jika skor kinerja kurang dari 60
        return 0  # Tidak ada potongan jika skor >= 60

    def laporan_kinerja(self):
        """
        Mengembalikan laporan kinerja bulanan dan peringkat karyawan berdasarkan skor total.
        :return: dict, data laporan kinerja dalam format {id_karyawan: skor_total}
        """
        peringkat = sorted(
            self.data_penilaian.items(),
            key=lambda x: x[1]['skor_total'],
            reverse=True
        )

        print("Laporan Kinerja Bulanan")
        print("==================================================================================")
        for idx, (id_karyawan, data) in enumerate(peringkat, start=1):
            print(
                f"{idx}. ID: {id_karyawan} | Kehadiran: {data['kehadiran']:.2f} poin "
                f"| Target: {data['target']} poin | Lembur: {data['lembur']} poin | "
                f"Skor Total: {data['skor_total']:.2f}"
            )

        # Mengembalikan laporan sebagai dictionary
        return {id_karyawan: data['skor_total'] for id_karyawan, data in peringkat}

    def ambil_skor_kinerja(self, id_karyawan):
        """
        Mengambil skor total kinerja untuk karyawan tertentu.
        :param id_karyawan: str, ID karyawan
        :return: float, skor total kinerja
        """
        if id_karyawan not in self.data_penilaian:
            return 0  # Jika tidak ada data, skor dianggap nol
        return self.data_penilaian[id_karyawan]['skor_total']
