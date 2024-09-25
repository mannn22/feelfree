print('mencari luas gabungan')
def luas_persegi_panjang():
    global luas_bangun_persegi_panjang
    lebar = int(input('lebar persegi panjang:'))
    panjang = int(input('panjang persegi panjang:'))
    luas_bangun_persegi_panjang = panjang * lebar
    print('=====================================')
    print('luas persegi panjang', luas_bangun_persegi_panjang)
    return luas_persegi_panjang
print('##################################################')

def luas_set_lingkaran():
    global luas_bangun_set_lingkaran
    jari_jari = int(input('masukan jari-jari lingkaran:'))
    luas_bangun_set_lingkaran = 22/7 * jari_jari * jari_jari /2
    print('=====================================')
    print('luas setengah lingkaran', luas_bangun_set_lingkaran)
    return luas_set_lingkaran
print('##################################################')

def luas_persegi():
    global luas_bangun_persegi
    sisi = int(input('masukan panjang sisi persegi:'))
    luas_bangun_persegi = sisi * sisi
    print('=====================================')
    print('luas persegi', luas_bangun_persegi)
    return luas_persegi
print('##################################################')

def gabungan():
    keseluruhan = luas_bangun_persegi + luas_bangun_persegi_panjang + luas_bangun_set_lingkaran
    print("Luas keseluruhan ",keseluruhan)
    return gabungan

luas_persegi_panjang()
luas_set_lingkaran()
luas_persegi()
gabungan()










