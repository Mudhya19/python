# format string

# contoh generic
# string
nama = "Ucup"
format_str = f"Hello {nama}"

print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# boolean
boolean = False
format_str = f"Boolean = {boolean}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"Bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:9.3f}"
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:010.3f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+d}"

print(format_minus)
print(format_plus)

# memformat persen
persentasi = 0.045
format_persen = f"persen = {persentasi:.2%}"

print(format_persen)

# Melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5

format_string = f"Harga total = Rp. {harga*jumlah:,}"
print(format_string)

# format angka lain (Binary, Octal, hexadecimal)

angka = 225
format_binary = f"binary = {bin(angka)}"
format_octal = f"binary = {oct(angka)}"
format_hexadecimal = f"binary = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexadecimal)
