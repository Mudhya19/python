# operasi aritmatika
a = 10
print("Nilai a  = ", a)
a += 1
print("Nilai a += ", a, "Nilai a menjadi ", a)
a -= 2
print("Nilai a -= ", a, "Nilai a menjadi ", a)
a *= 5
print("Nilai a *= ", a, "Nilai a menjadi ", a)
a /= 2
print("Nilai a /= ", a, "Nilai a menjadi ", a)

b = 10
print("\nNilai b  = ", b)
b %= 3
print("Nilai b %= 3 ", "Nilai b menjadi ", b)
b = 10
print("\nNilai b = ", b)
b //= 3
print("Nilai b //=  3", "Nilai b menjaid ", b)
b = 5
print("\nNilai b  = ", b)
b **= 5
print("Nilai b **= 5", "Nilai b menjadi ", b)

# operasi bitwise
c = True
print("\nNila c  = ", )
c |= False
print("Nilai c |= ", c, "Nilai c menjadi ", c)
c = False
print("Nilai c  = ", c)
c |= False
print("Nilai c |= ", c, "Nilai c menjadi ", c)

c = True
print("\nNilai c  = ", c)
c &= False
print("Nilai c &= ", c, "Nilai c menjadi ", c)
c = False
print("Nila c  = ", c)
c &= False
print("Nilai c &= ", c, "Nilai c menjadi ", c)

c = True
print("\nNila c  = ", c)
c ^= False
print("Nila c ^= ", c, "Nila c menjadi ", c)
c = True
print("Nila c  = ", c)
c ^= True
print("Nilai c ^= ", c, "Nilai c menjadi ", c)

# shift
d = 0b0100
print("\nNilai d  = ", format(d, '04b'))
d >>= 2
print("Nilai d >>= 2", "Nilai d menjadi ", format(d, '04b'))
d <<= 1
print("Nilai d <<= 1", "Nilai d menjadi ", format(d, '04b'))
