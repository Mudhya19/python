# 1. operasi penambahan string
nama_awal = "amat"
nama_tengah = "p"
nama_akhir = "ramuka"

nama_lengkap = (nama_awal + " " + nama_tengah + "'" + nama_akhir)
print("perkenalkan nama saya", nama_lengkap)

# 2. operasi perhitungan string di dalam string
data = len(nama_lengkap)
print("jumlah dalam nama adalah", data)

# 3. operasi untuk string

# a.mengecek apakah ada komponen char atau string didalam string

d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

a = "a"
status = a in nama_lengkap
print(a + " ada di " + nama_lengkap + " = " + str(status))

A = "A"
status = A not in nama_lengkap
print (A + " Tidak ada di " + nama_lengkap + " = " + str(status))

# b.perulangan string
print("wkwk"*5)
print(10*"wkwk")

# c.indexing
print("index ke 0 : " + nama_lengkap[0])
print("index ke 1 : " + nama_lengkap[1])
print("index ke-3 : " + nama_lengkap[-3])
print("index ke 0,3 : " + nama_lengkap[0:4])
print("index ke 3,8 : " + nama_lengkap[3:9])
print("index ke 0,2,4,6,8,10,12 : "+nama_lengkap[0:13:2])

# d.item kecil
print("paling kecil : " + min(nama_lengkap))
# e.item besar
print("paling besar : " + max(nama_lengkap))

asscii_code = ord(" ")
print("ASSCII CODE untuk spasi adalah " + str(asscii_code))
data = 96
print("char untuk ASSCI 122 adalah " + chr(data))

# 4. operasi method
data = "astaga naga mana naganya"
jumlah = data.count(a)
print("jumlah a pada kalimat di " + data + " = " + str(jumlah))
