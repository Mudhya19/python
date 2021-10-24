angka = 0

while angka < 5:
    print('Nilai angka adalah: ', angka)
    angka = angka + 1

print('Diluar while')

start = True
angka = 0

while start:  # Variable Boolean
    print('Dalam while')
    if angka == 100:
        start = False
        print('Angka 100 Ditemukan')
    angka += 1
print('Dilua while')
