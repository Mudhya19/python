barang = ['Gayung', 'ember', 'sabun', 'shampo', 'conditioner']
print(barang)

# beberepa method yang bisa digunakan untuk manipulasi list
barang.append('keran')
print(barang)

barang.extend('sabun cuci')
print(barang)

barang.insert(2, 'pembersih lantai')
print(barang)

# method untuk menghitung anggota
jumlahSepeda = barang.count('keran')
print("Jumlah sepeda adalah: ", jumlahSepeda)

# meremove atau menghapus data
barang.remove('keran')
print(barang)

barang.reverse()
print(barang)

print("="*75)
stuff = barang.copy()
stuff.append('wash hand')
print(stuff)
print(barang)
