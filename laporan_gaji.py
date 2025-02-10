class LaporanGaji:
    @staticmethod
    def buat_laporan_karyawan(karyawan, gaji, penilaian_kinerja, karyawan_id):
        karyawan_data = karyawan.ambil_karyawan(karyawan_id)
        if not karyawan_data:
            return f"Karyawan dengan ID {karyawan_id} tidak ditemukan."

        # Data gaji pokok
        gaji_pokok = gaji.data_gaji[karyawan_id]

        # Komponen perhitungan
        bonus = penilaian_kinerja.hitung_bonus(id_karyawan=karyawan_id) * gaji_pokok  # Nominal bonus
        potongan_absensi = penilaian_kinerja.hitung_potongan(id_karyawan=karyawan_id)
        potongan_asuransi = gaji_pokok * 0.02  # Sudah didefinisikan di gaji.py
        skor_kinerja = penilaian_kinerja.ambil_skor_kinerja(karyawan_id)  # Ambil skor kinerja
        potongan_kinerja = 500000 if skor_kinerja < 60 else 0  # Potongan jika skor < 60

        # Total potongan dan gaji bersih
        total_potongan = potongan_asuransi + potongan_absensi + potongan_kinerja
        gaji_bersih = gaji_pokok + bonus - total_potongan

        # Format laporan karyawan
        laporan = (
            f"=============================\n"
            f"Laporan Gaji Karyawan\n"
            f"=============================\n"
            f"ID Karyawan: {karyawan_id}\n"
            f"Nama: {karyawan_data.nama}\n"
            f"Jabatan: {karyawan_data.jabatan}\n"
            f"Gaji Pokok: Rp{gaji_pokok:,}\n"
            f"Bonus: Rp{bonus:,.0f}\n"
            f"Potongan Asuransi: Rp{potongan_asuransi:,}\n"
            f"Potongan Absensi: Rp{potongan_absensi:,}\n"
            f"Potongan Kinerja: Rp{potongan_kinerja:,} (Skor Kinerja: {skor_kinerja})\n"
            f"Total Potongan: Rp{total_potongan:,}\n"
            f"Gaji Bersih: Rp{gaji_bersih:,}\n"
            f"=============================\n"
        )
        return laporan

    @staticmethod
    def buat_laporan_atasan(karyawan, gaji, penilaian_kinerja):
        # Header tabel
        laporan = (
            f"{'ID Karyawan':<12}{'Nama':<20}{'Jabatan':<20}{'Gaji Pokok':<15}"
            f"{'Bonus':<15}{'P.Asuransi':<12}{'P.Absensi':<12}{'P.Kinerja':<12}{'Gaji Bersih':<15}\n"
            f"{'-' * 123}\n"
        )

        for karyawan_id in gaji.data_gaji.keys():
            karyawan_data = karyawan.ambil_karyawan(karyawan_id)
            if not karyawan_data:
                laporan += f"{karyawan_id:<12}{'Data Tidak Ditemukan':<20}\n"
                continue

            # Data gaji pokok
            gaji_pokok = gaji.data_gaji[karyawan_id]

            # Komponen perhitungan
            bonus = penilaian_kinerja.hitung_bonus(id_karyawan=karyawan_id) * gaji_pokok  # Nominal bonus
            potongan_absensi = penilaian_kinerja.hitung_potongan(id_karyawan=karyawan_id)
            potongan_asuransi = gaji_pokok * 0.02  # Sudah didefinisikan di gaji.py
            skor_kinerja = penilaian_kinerja.ambil_skor_kinerja(karyawan_id)  # Ambil skor kinerja
            potongan_kinerja = 500000 if skor_kinerja < 60 else 0  # Potongan jika skor < 60

            # Total potongan dan gaji bersih
            total_potongan = potongan_asuransi + potongan_absensi + potongan_kinerja
            gaji_bersih = gaji_pokok + bonus - total_potongan

            # Tambahkan data karyawan ke tabel
            laporan += (
                f"{karyawan_id:<12}{karyawan_data.nama:<20}{karyawan_data.jabatan:<20}"
                f"Rp{gaji_pokok:<12,}Rp{bonus:<12,.0f}Rp{potongan_asuransi:<10,.0f}Rp{potongan_absensi:<10,.0f}"
                f"Rp{potongan_kinerja:<10,.0f}Rp{gaji_bersih:<12,}\n"
            )

        # Penutup tabel
        laporan += f"{'-' * 123}\n"
        return laporan
