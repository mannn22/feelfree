class Pegawai:
    def __init__(self, nik, nama, alamat):
        self.nik = nik
        self.nama = nama
        self.alamat = alamat

class Produk:
    def __init__(self, kode_produk, nama_produk, harga, jenis_produk):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.harga = harga
        self.jenis_produk = jenis_produk

    def tampilkan_info(self):
        return f"{self.jenis_produk} - {self.nama_produk}: Rp{self.harga}"

class Snack(Produk):
    def __init__(self, kode_produk, nama_snack, harga):
        super().__init__(kode_produk, nama_snack, harga, "Snack")

class Makanan(Produk):
    def __init__(self, kode_produk, nama_makanan, harga):
        super().__init__(kode_produk, nama_makanan, harga, "Makanan")

class Minuman(Produk):
    def __init__(self, kode_produk, nama_minuman, harga):
        super().__init__(kode_produk, nama_minuman, harga, "Minuman")

class Transaksi:
    def __init__(self, no_transaksi, pegawai):
        self.no_transaksi = no_transaksi
        self.pegawai = pegawai
        self.produk_list = []
        self.total_harga = 0

    def tambah_produk(self, produk, jumlah):
        self.produk_list.append((produk, jumlah))
        self.total_harga += produk.harga * jumlah

    def cetak_struk(self):
        print("\n=== STRUK PEMBELIAN ===")
        print(f"No Transaksi: {self.no_transaksi}")
        print(f"Nama Pegawai: {self.pegawai.nama}")
        print(f"Alamat Pegawai: {self.pegawai.alamat}")
        print("\nDaftar Produk:")
        for produk, jumlah in self.produk_list:
            print(f"- {produk.nama_produk} x{jumlah} : Rp{produk.harga * jumlah}")
        print(f"\nTotal Harga: Rp{self.total_harga}")
        print("=======================\n")

    def tampilkan_ringkasan(self):
        return f"No Transaksi: {self.no_transaksi}, Total Harga: Rp{self.total_harga}"

def menu():
    pegawai = Pegawai("013", "Alif", "Jl. Kalirang")
    produk_list = [
        Snack("S001", "Keripik Singkong", 10000),
        Snack("S002", "Risol Mayo", 12000),
        Makanan("M001", "Nasi Goreng", 20000),
        Makanan("M002", "Kwetiau", 25000),
        Minuman("D001", "Teh Botol", 5000),
        Minuman("D002", "Milk Tea", 7000),
    ]
    
    daftar_transaksi = []

    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Buat Transaksi dan Tambah Produk")
        print("2. Cetak Struk Transaksi Terakhir")
        print("3. Tampilkan Semua Transaksi")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            no_transaksi = input("Masukkan No Transaksi: ")
            transaksi = Transaksi(no_transaksi, pegawai)
            daftar_transaksi.append(transaksi)
            print("Transaksi baru berhasil dibuat.")
            
            while True:
                print("\nDaftar Produk:")
                for i, produk in enumerate(produk_list):
                    print(f"{i + 1}. {produk.tampilkan_info()}")

                pilihan_produk = int(input("Pilih produk (nomor, atau 0 untuk selesai): ")) - 1
                if pilihan_produk == -1:
                    break

                jumlah = int(input("Masukkan jumlah: "))

                if 0 <= pilihan_produk < len(produk_list):
                    transaksi.tambah_produk(produk_list[pilihan_produk], jumlah)
                    print("Produk berhasil ditambahkan ke transaksi.")
                else:
                    print("Pilihan produk tidak valid.")
            
        elif pilihan == "2":
            if not daftar_transaksi:
                print("Belum ada transaksi yang dibuat!")
            else:
                daftar_transaksi[-1].cetak_struk()

        elif pilihan == "3":
            if not daftar_transaksi:
                print("Belum ada transaksi yang dibuat!")
            else:
                print("\n=== DAFTAR SELURUH TRANSAKSI ===")
                for idx, transaksi in enumerate(daftar_transaksi, start=1):
                    print(f"{idx}. {transaksi.tampilkan_ringkasan()}")

        elif pilihan == "4":
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid.")

menu()
