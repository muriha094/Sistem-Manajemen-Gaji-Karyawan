from absensi import Absensi
from gaji import Gaji
from karyawan import ManajemenKaryawan
from laporan_gaji import LaporanGaji
from laporan_absensi import LaporanAbsensi
from penilaian_kinerja import PenilaianKinerja


class LoginSystem:
    def __init__(self):
        self.users = {
            "admin": {"password": "admin123", "role": "atasan"},
            "user": {"password": "user123", "role": "karyawan"},
        }

    def login(self):
        print("=== Login ke Sistem Penggajian Karyawan ===")
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()

        if username in self.users and self.users[username]["password"] == password:
            role = self.users[username]["role"]
            print(f"Login berhasil sebagai {role.capitalize()}\n")
            return role
        else:
            print("Username atau password salah.\n")
            return None


def menu_karyawan(gaji, penilaian_kinerja, karyawan, karyawan_id):
    if karyawan_id not in karyawan.daftar_karyawan:
        print("ID Karyawan tidak ditemukan.")
        return

    while True:
        print("\n=== Menu Karyawan ===")
        print("1. Lihat Gaji Bulan ini")
        print("2. Lihat Laporan Kinerja bulan ini")
        print("3. Logout")
        print("4. Keluar Sistem")

        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            print(
                LaporanGaji.buat_laporan_karyawan(
                    karyawan, gaji, penilaian_kinerja, karyawan_id
                )
            )
        elif pilihan == "2":
            penilaian_kinerja.laporan_kinerja()
        elif pilihan == "3":
            print("Logout berhasil. Silakan login kembali.")
            break
        elif pilihan == "4":
            print("Keluar dari sistem. Sampai jumpa!")
            exit()
        else:
            print("Pilihan tidak valid. Harap pilih opsi yang tersedia.")


def menu_atasan(gaji, penilaian_kinerja, absensi, karyawan):
    while True:
        print("\n=== Menu Atasan ===")
        print("1. Tambah Karyawan")
        print("2. Hapus Karyawan")
        print("3. Input Absensi dan Penilaian Kinerja")
        print("4. Laporan Gaji")
        print("5. Laporan Absensi")
        print("6. Laporan Kinerja Bulanan")
        print("7. Logout")
        print("8. Keluar Sistem")

        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            id_karyawan = input("Masukkan ID Karyawan: ").strip()
            nama = input("Masukkan Nama Karyawan: ").strip()
            pilihan_jabatan = input(
                "Masukkan Pilihan Jabatan (a - Direktur, b - Manajer, c - Supervisor, d - Staf Administrasi, e - Desain Grafis): "
            ).strip().lower()
            karyawan.tambah_karyawan(id_karyawan, nama, pilihan_jabatan)
            karyawan_data = karyawan.ambil_karyawan(id_karyawan)
            gaji.tambah_karyawan(id_karyawan, karyawan_data.gaji_pokok)
            print("Karyawan berhasil ditambahkan.")

        elif pilihan == "2":
            id_karyawan = input("Masukkan ID Karyawan yang akan dihapus: ").strip()
            karyawan.hapus_karyawan(id_karyawan)
            gaji.hapus_karyawan(id_karyawan)
            print("Karyawan berhasil dihapus.")

        elif pilihan == "3":
            id_karyawan = input("Masukkan ID Karyawan: ").strip()
            try:
                kehadiran = int(input("Masukkan Kehadiran (0-30 hari): "))
                target = int(input("Masukkan Skor Target Kerja (0-100 poin): "))
                lembur = int(input("Masukkan Jumlah Jam Lembur (0-100 jam per bulan): "))
                if not (0 <= kehadiran <= 30 and 0 <= target <= 100 and 0 <= lembur <= 100):
                    raise ValueError
            except ValueError:
                print("Input tidak valid. Harap masukkan nilai numerik yang sesuai.")
                continue

            absensi.tambah_absensi(id_karyawan, kehadiran)
            penilaian_kinerja.beri_penilaian(id_karyawan, kehadiran, target, lembur)
            print("Data absensi dan penilaian berhasil diperbarui.")

        elif pilihan == "4":
            print(LaporanGaji.buat_laporan_atasan(karyawan, gaji, penilaian_kinerja))

        elif pilihan == "5":
            print(LaporanAbsensi.buat_laporan_absensi(absensi))

        elif pilihan == "6":
            penilaian_kinerja.laporan_kinerja()

        elif pilihan == "7":
            print("Logout berhasil. Silakan login kembali.")
            return

        elif pilihan == "8":
            print("Keluar dari sistem. Sampai jumpa!")
            exit()

        else:
            print("Pilihan tidak valid. Harap pilih opsi yang tersedia.")


if __name__ == "__main__":
    absensi = Absensi()
    gaji = Gaji()
    karyawan = ManajemenKaryawan()
    penilaian_kinerja = PenilaianKinerja()

    login_system = LoginSystem()
    role = None

    while True:
        while role is None:
            role = login_system.login()

        if role == "karyawan":
            karyawan_id = input("Masukkan ID Karyawan Anda: ").strip()
            menu_karyawan(gaji, penilaian_kinerja, karyawan, karyawan_id)

        elif role == "atasan":
            menu_atasan(gaji, penilaian_kinerja, absensi, karyawan)

        role = None
