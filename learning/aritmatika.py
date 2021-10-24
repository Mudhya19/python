# operasi aritmatika
a = 10
b = 3

# operasi tambahan
hasil = 10 + 3
print(a, '+', b, '=', hasil)

# operasi pengurangan
hasil = 10 - 3
print(a, '-', b, '=', hasil)

# operasi perkalian
hasil = 10 * 3
print(a, '*', b, '=', hasil)

# operasi pembagian
hasil = 10 / 3
print(a, '/', b, '=', hasil)

# operasi eksponen (pangkat)
hasil = a**b
print(a, '**', b, '=', hasil)

# operasi modulus
hasil = a % b
print(a, '%', b, '=', hasil)

# operasi floor division
hasil = a // b
print(a, '//', b, '=', hasil)

# priotas operasi
'''
    1. ()
    2. exponen **
    3. perkalian dan teman-teman * / ** % //
    4. pertambahan dan pengurangan + -
'''

x = 33
y = 2
z = 6

hasil = x ** y * (z + x) / y - y % z // x
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x, '=', hasil)

hasil = x + y * z
print(x, '+', y, '*', z, '=', hasil)

# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z
print('(', x, '+', y, ') * ', z, '=', hasil)

hasil = (x * z) * y
print('(', x, '*', z, ')*', y, '=', hasil)

hasil = (x - z) ** y
print('(', x, '-', z, ')**', y, '=', hasil)
