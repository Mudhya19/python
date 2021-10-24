a = 9
b = 5

# operasi bitwise or
print('============= OR =============')
c = a | b
print('Nilai : ', a, 'Binary : ', format(a, '08b'))
print('Nilai : ', b, 'Binary : ', format(b, '08b'))
print('==========================( | )')
print('Nilai : ', c, 'Binary : ', format(c, '08b'))

# operasi bitwise and
print('============= AND ============')
c = a & b
print('Nilai : ', a, 'Binary : ', format(a, '08b'))
print('Nilai : ', b, 'Binary : ', format(b, '08b'))
print('==========================( & )')
print('Nilai : ', c, 'Binary : ', format(c, '08b'))

# operasi bitwise XOR
print('============= XOR ============')
c = a ^ b
print('Nilai : ', a, 'Binary : ', format(a, '08b'))
print('Nilai : ', b, 'Binary : ', format(b, '08b'))
print('==========================( ^ )')
print('Nilai : ', c, 'Binary : ', format(c, '08b'))

# operasi bitwise NOT
print('============= NOT ============')
c = ~ a
print('Nilai : ', a, 'Binary : ', format(a, '08b'))
print('==========================( ~ )')
print('Nilai : ', c, 'Binary : ', format(c, '08b'))
d = 0b00001010
e = 0b11111111
print('Nilai : ', d ^ e, 'Binary : ', format(d ^ e, '08b'))

print('=========== SHIFT << ==========')
c = a >> 1
print('Nilai : ', a, 'Binary : ', format(a, '08b'))
print('==========================( >> )')
print('Nilai : ', c, 'Binary : ', format(c, '08b'))

print('=========== SHIFT << =========')
c = a << 2
print('Nilai : ', a, 'Binary : ', format(a, '08b'))
print('==========================( << )')
print('Nilai : ', c, 'Binary : ', format(c, '08b'))
