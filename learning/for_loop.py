# list sebagai iterable
gorengan = ['bakwan', 'cireng', 'tahu isi', 'tempe goreng', 'ubi goreng']

for g in gorengan:
    print(g)
    print(len(g))

# string sebagai iterable
bakwan = 'bakwan'

for i in bakwan:
    print(i)

# for didalam for
gorengan = ['bakwan', 'cireng', 'tahu isi', 'tempe goreng', 'ubi goreng']
buah = ['semangka', 'jeruk', 'apel', 'anggur']
sayur = ['kangkung', 'wortel', 'tomat', 'kentang']

Daftar_belanja = [gorengan, buah, sayur]

for subDaftarBelanjar in Daftar_belanja:
    print(subDaftarBelanjar)
    for kompenen in subDaftarBelanjar:
        print(kompenen)
