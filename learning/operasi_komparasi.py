a = 5
b = 3

print('======== lebih dari (>)')

hasil = b > 2
print(b, ' > ', 2, '=', hasil)
hasil = b > 6
print(b, ' > ', 6, '=', hasil)
hasil = a > 5
print(a, ' > ', 5, '=', hasil)

print('======== kurang dari (<)')

hasil = b < 2
print(b, '< ', 2, '=', hasil)
hasil = b < 6
print(b, ' < ', 6, '=', hasil)
hasil = a < 5
print(a, ' < ', 5, '=', hasil)

print('======== lebih dari sama dengan (>=)')

hasil = b >= 2
print(b, ' >= ', 2, '=', hasil)
hasil = b >= 6
print(b, ' >= ', 6, '=', hasil)
hasil = a >= 5
print(a, ' >= ', 5, '=', hasil)

print('======== kurang dari sama dengan (=<)')

hasil = b <= 2
print(b, '<= ', 2, '=', hasil)
hasil = b <= 6
print(b, ' <= ', 6, '=', hasil)
hasil = a <= 5
print(a, ' <= ', 5, '=', hasil)


print('======== sama dengan (==)')

hasil = b == 2
print(b, '== ', 2, '=', hasil)
hasil = b == 6
print(b, ' == ', 6, '=', hasil)
hasil = a == 5
print(a, ' == ', 5, '=', hasil)

print('======== tidak sama dengan (!=)')

hasil = b != 2
print(b, '!= ', 2, '=', hasil)
hasil = b != 6
print(b, ' != ', 6, '=', hasil)
hasil = a != 5
print(a, ' != ', 5, '=', hasil)

print('======== identity object (is)')
x = 5
y = 5
print('Nilai x =', x, ',id = ', hex(id(x)))
print('Nilai y =', y, ',id = ', hex(id(y)))
hasil = x is y
print('Nilai x is y =', hasil)

x = 5
y = 6
print('Nilai x =', x, ',id = ', hex(id(x)))
print('Nilai y =', y, ',id = ', hex(id(y)))
hasil = x is y
print('Nilai x is y =', hasil)

print('======== identity object (is not)')
x = 5
y = 5
print('Nilai x =', x, ',id = ', hex(id(x)))
print('Nilai y =', y, ',id = ', hex(id(y)))
hasil = x is not y
print('Nilai x is not y =', hasil)

x = 5
y = 6
print('Nilai x =', x, ',id = ', hex(id(x)))
print('Nilai y =', y, ',id = ', hex(id(y)))
hasil = x is not y
print('Nilai x is not y =', hasil)
