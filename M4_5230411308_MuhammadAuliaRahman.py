debitur_list = []
pinjaman_list = []

def tampilkan_debitur():
    if not debitur_list:
        print("Tidak ada debitur yang terdaftar.")
        return
    print("Daftar Debitur:")
    for debitur in debitur_list:
        print(f"Nama: {debitur['nama_public']} | KTP: {debitur['ktp']} | Limit Pinjaman: {debitur['limit_pinjaman']}")

def cari_debitur(nama):
    for debitur in debitur_list:
        if debitur["nama_public"] == nama or debitur["nama_private"] == nama:
            return debitur
    return None

def tambah_debitur(nama_public, nama_private, ktp, limit_pinjaman):
    for debitur in debitur_list:
        if debitur["ktp"] == ktp:
            print(f"Debitur dengan KTP {ktp} sudah ada.")
            return
    debitur_baru = {
        "nama_public": nama_public,
        "nama_private": nama_private,
        "ktp": ktp,
        "limit_pinjaman": limit_pinjaman
    }
    debitur_list.append(debitur_baru)
    print(f"Debitur {nama_public} berhasil ditambahkan.")

def tambah_pinjaman(nama_debitur, pinjaman, bunga, bulan):
    debitur = cari_debitur(nama_debitur)
    if not debitur:
        print(f"Debitur dengan nama {nama_debitur} tidak ditemukan.")
        return

    if pinjaman > debitur["limit_pinjaman"]:
        print(f"Jumlah pinjaman melebihi limit untuk debitur {nama_debitur}.")
        return
    
    angsuran_pokok = pinjaman * (bunga / 100)
    angsuran_bulanan = angsuran_pokok / bulan
    total_angsuran = angsuran_pokok * angsuran_bulanan

    pinjaman = {
        "nama_debitur": nama_debitur,
        "pinjaman": pinjaman,
        "bunga": bunga,
        "bulan": bulan,
        "angsuran_pokok": angsuran_pokok, 
        "angsuran_bulanan": angsuran_bulanan, 
        "total_angsuran": total_angsuran
    }
    pinjaman_list.append(pinjaman)
    print(f"Pinjaman sebesar {pinjaman} untuk {nama_debitur} berhasil ditambahkan.")

def tampilkan_pinjaman():
    if not pinjaman_list:
        print("Tidak ada pinjaman yang terdaftar.")
        return
    print("Daftar Pinjaman:")
    for pinjaman in pinjaman_list:
        print(f"Nama Debitur: {pinjaman['nama_debitur']} | Pinjaman: {pinjaman['pinjaman']} | Bunga: {pinjaman['bunga']}% | Tenor: {pinjaman['bulan']} | Angsuran pokok:{pinjaman['angsuran_pokok']} | Angsuran Bulanan:{pinjaman['angsuran_bulanan']} | Total Angsuran:{pinjaman['total_angsuran']} ")

def kelola_debitur():
    while True:
        print("\n--- Kelola Debitur ---")
        print("1. Tampilkan Daftar Debitur")
        print("2. Tambah Debitur")
        print("3. Cari Debitur")
        print("4. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_debitur()
        elif pilihan == "2":
            nama_public = input("Masukkan nama public debitur: ")
            nama_private = input("Masukkan nama private debitur: ")
            ktp = input("Masukkan nomor KTP: ")
            limit_pinjaman = int(input("Masukkan limit pinjaman: "))
            tambah_debitur(nama_public, nama_private, ktp, limit_pinjaman)
        elif pilihan == "3":
            nama = input("Masukkan nama debitur (public atau private): ")
            debitur = cari_debitur(nama)
            if debitur:
                print(f"Nama Public: {debitur['nama_public']}, Nama Private: {debitur['nama_private']}, KTP: {debitur['ktp']}, Limit Pinjaman: {debitur['limit_pinjaman']}")
            else:
                print(f"Debitur dengan nama {nama} tidak ditemukan.")
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

def kelola_pinjaman():
    while True:
        print("\n--- Kelola Pinjaman ---")
        print("1. Tampilkan Daftar Pinjaman")
        print("2. Tambah Pinjaman")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_pinjaman()
        elif pilihan == "2":
            nama_debitur = input("Masukkan nama debitur: ")
            jumlah_pinjaman = int(input("Masukkan jumlah pinjaman: "))
            bunga = float(input("Masukkan bunga (%): "))
            bulan = int(input("Masukkan tenor (bulan): "))
            tambah_pinjaman(nama_debitur, jumlah_pinjaman, bunga, bulan)
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

while True:
    print("\n--- Menu Utama ---")
    print("1. Kelola Debitur")
    print("2. Kelola Pinjaman")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        kelola_debitur()
    elif pilihan == "2":
        kelola_pinjaman()
    elif pilihan == "3":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
