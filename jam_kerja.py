# jam_kerja.py
class JamKerja:
    def __init__(self, id_karyawan, jam_per_hari):
        self.id_karyawan = id_karyawan
        self.jam_per_hari = jam_per_hari
    
    def hitung_bonus(self, gaji_pokok):
        if self.jam_per_hari > 8:
            return gaji_pokok * 0.2
        return 0