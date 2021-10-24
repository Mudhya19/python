# operasi_dan_manipulasi(method)

# merubah semua ke uppercase
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "aku keCe AbbiIIIZZZ"
print("Normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

# pengecekan dengan isx method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower()
print(salam + " is lower = " + str(apakah_lower))
# contoh pengecekan upper case
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalpha <----- untuk mengecek semuanya huruf
# isalnum <----- huruf dan angka
# isdecimal <----- angka saja
# isspace <------ spasi, tab , newline \n
# istitle <----- semua kata dimulai dengan huruf besar
# isdigit <----- mendeteksi string yang terdiri dari angka saja.
# swapcase <-----digunakan untuk mengkonversi string huruf besar dan huruf kecil.

judul = "Is It Okay Not To Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

# pengecekan komponen startswith() and endswith() <---- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppa".endswith("Oppa")
print("end = " + str(cek_end))

# penggabungan komponen join() dan split()
pisah = ['aku', 'sayang', 'kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))


# alokasi karakter rjust(), ljust(), dan center()
print(5*"=" + "data" + "="*5)
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10, ":")
print("'"+tengah+"'")

# kebalikannya strip()
tengah = "tengah".strip(":")
print("'"+tengah+"'")
