import mysql.connector

conn = mysql.connector.connect(
    user = "root",
    host = "localhost",
    password = "",
    database = "penjualan"
)

cur = conn.cursor()

#membuat database
# cur.execute("CREATE DATABASE pejualan")

cur.execute('DROP TABLE IF EXISTS Struk')
cur.execute('DROP TABLE IF EXISTS Transaksi')
cur.execute('DROP TABLE IF EXISTS Produk')
cur.execute('DROP TABLE IF EXISTS Pegawai')

# # Membuat tabel Pegawai
cur.execute("""
CREATE TABLE IF NOT EXISTS Pegawai (
    NIK VARCHAR(7) NOT NULL PRIMARY KEY,
    Nama VARCHAR(25),     
    Alamat VARCHAR(225)
)
""")

# # Membuat tabel Produk
cur.execute("""
CREATE TABLE IF NOT EXISTS Produk (
    Kode_Produk CHAR(10) NOT NULL PRIMARY KEY,
    Nama_Produk VARCHAR(10),
    Jenis_produk VARCHAR(225),
    Harga DECIMAL(10, 2)
)
""")

# # Membuat tabel Transaksi
cur.execute("""
CREATE TABLE IF NOT EXISTS Transaksi (
    No_Transaksi INT NOT NULL PRIMARY KEY,
    Detail_Transaksi CHAR(10) NOT NULL,
    NIK VARCHAR(7),
    FOREIGN KEY (NIK) REFERENCES Pegawai(NIK)
)
""")

# # Membuat tabel Struk
cur.execute("""
CREATE TABLE IF NOT EXISTS Struk (
    No_Transaksi INT NOT NULL PRIMARY KEY,
    Nama_pegawai VARCHAR(25),
    Nama_Produk VARCHAR(25),
    Kode_Produk CHAR(10),
    Jumlah_Produk INT(15),
    Total_Harga DECIMAL(10, 2),
    FOREIGN KEY (Kode_Produk) REFERENCES Produk(Kode_Produk),
    FOREIGN KEY (No_Transaksi) REFERENCES Transaksi(No_Transaksi)
)
""")

# Membuat menu utama
def tampil_data():
    tabel = input("Masukkan nama tabel (Pegawai/Produk/Transaksi/Struk): ")
    cur.execute(f"SELECT * FROM {tabel}")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def input_semua_data():
    # Input data untuk semua tabel
    tambah_pegawai()
    tambah_produk()
    tambah_transaksi()
    tambah_struk()

def input_data_tertentu():
    tabel = input("Masukkan nama tabel untuk input data (Pegawai/Produk/Transaksi/Struk): ")
    if tabel.lower() == "pegawai":
        tambah_pegawai()
    elif tabel.lower() == "produk":
        tambah_produk()
    elif tabel.lower() == "transaksi":
        tambah_transaksi()
    elif tabel.lower() == "struk":
        tambah_struk()
    else:
        print("Tabel tidak valid.")

def ubah_data():
    tabel = input("Masukkan nama tabel untuk ubah data (Pegawai/Produk/Transaksi/Struk): ")
    kolom = input("Masukkan kolom yang ingin diubah: ")
    nilai_baru = input("Masukkan nilai baru: ")
    kondisi = input("Masukkan kondisi (contoh: NIK='123'): ")
    cur.execute(f"UPDATE {tabel} SET {kolom} = '{nilai_baru}' WHERE {kondisi}")
    conn.commit()
    print("Data berhasil diubah.")

def hapus_data():
    tabel = input("Masukkan nama tabel untuk hapus data (Pegawai/Produk/Transaksi/Struk): ")
    kondisi = input("Masukkan kondisi (contoh: NIK='123'): ")
    cur.execute(f"DELETE FROM {tabel} WHERE {kondisi}")
    conn.commit()
    print("Data berhasil dihapus.")

def tambah_pegawai():
    nik = input("Masukkan NIK: ")
    cur.execute("SELECT * FROM Pegawai WHERE NIK = %s", (nik,))
    if cur.fetchone():
        print("NIK sudah ada dalam database. Silakan gunakan NIK lain atau perbarui data yang sudah ada.")
    else:
        nama = input("Masukkan Nama: ")
        alamat = input("Masukkan Alamat: ")
        cur.execute("INSERT INTO Pegawai (NIK, Nama, Alamat) VALUES (%s, %s, %s)", (nik, nama, alamat))
        conn.commit()
        print("Data Pegawai berhasil ditambahkan.")

def tambah_produk():
    kode_produk = input("Masukkan Kode Produk: ")
    nama_produk = input("Masukkan Nama Produk: ")
    jenis_produk = input("Masukkan Jenis Produk: ")
    harga = float(input("Masukkan Harga: "))
    cur.execute("INSERT INTO Produk (Kode_Produk, Nama_Produk, Jenis_produk, Harga) VALUES (%s, %s, %s, %s)", (kode_produk, nama_produk, jenis_produk, harga))
    conn.commit()
    print("Data Produk berhasil ditambahkan.")

def tambah_transaksi():
    no_transaksi = int(input("Masukkan Nomor Transaksi: "))
    detail_transaksi = input("Masukkan Detail Transaksi (Kode Produk): ")
    nik = input("Masukkan NIK Pegawai: ")
    cur.execute("INSERT INTO Transaksi (No_Transaksi, Detail_Transaksi, NIK) VALUES (%s, %s, %s)", (no_transaksi, detail_transaksi, nik))
    conn.commit()
    print("Data Transaksi berhasil ditambahkan.")

def tambah_struk():
    no_transaksi = int(input("Masukkan Nomor Transaksi: "))
    nama_pegawai = input("Masukkan Nama Pegawai: ")
    nama_produk = input("Masukkan Nama Produk: ")
    jumlah_produk = int(input("Masukkan Jumlah Produk: "))
    total_harga = float(input("Masukkan Total Harga: "))
    cur.execute("INSERT INTO Struk (NoTransaksi, Nama_pegawai, Nama_Produk, Jumlah_Produk, Total_Harga) VALUES (%s, %s, %s, %s, %s)", (no_transaksi, nama_pegawai, nama_produk, jumlah_produk, total_harga))
    conn.commit()
    print("Data Struk berhasil ditambahkan.")

# Menu utama
while True:
    print("\nMenu:")
    print("1. Tampil Data")
    print("2. Input Semua Data")
    print("3. Input Data Tertentu")
    print("4. Ubah Data")
    print("5. Hapus Data")
    print("6. Keluar")
    menu = input("Pilihan Menu: ")

    if menu == "1":
        tampil_data()
    elif menu == "2":
        input_semua_data()
    elif menu == "3":
        input_data_tertentu()
    elif menu == "4":
        ubah_data()
    elif menu == "5":
        hapus_data()
    elif menu == "6":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid.")
