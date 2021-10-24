# scope variable : global
namaKucing = 'cassandra'
makananKucing = "royal canin"


def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru
    print('Saya rubah nama kucing menjadi', namaKucing)


def kasihMakananKucing(makanan, nama):
    global namaKucing, makananKucing
    namaKucing = nama
    makananKucing = makanan


rubahNamaKucing('kittie')
kasihMakananKucing('Universal', 'alex')
print('nama kucing saya menjadi', namaKucing, 'dan makan', makananKucing)
