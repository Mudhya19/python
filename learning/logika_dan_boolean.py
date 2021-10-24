print("=====logika dan boolean=====")

print("=====NOT=====")
# NOT memastikan true atau false dalam suatu hasil
a = True
c = not a
print("Data : A ", a)
print("======NOT")
print("Data : C ", c)

print("=====AND=====")
# AND, jika salah satu false maka akan bernilai false, kecuali 2 kesamaan true
a = True
b = True
c = a and b
print(a, "AND", b, "=", c)
a = True
b = False
c = a and b
print(a, "AND", b, "=", c)
a = False
b = True
c = a and b
print(a, "AND", b, "=", c)
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)

print("=====OR=====")

# OR, jika true maka hasilnya true walaupun salah satunya, kecuali kesamaan nilai false
a = True
b = True
c = a or b
print(a, "OR", b, "=", c)
a = True
b = False
c = a or b
print(a, "OR", b, "=", c)
a = False
b = True
c = a or b
print(a, "OR", b, "=", c)
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)

print ("=====XOR=====")
# XOR, jika salah satunya true maka hasilnya true, kecuali kesamaan maka hasilnya false
a = True
b = True
c = a ^ b
print(a, "XOR", b, "=", c)
a = True
b = False
c = a ^ b
print(a, "XOR", b, "=", c)
a = False
b = True
c = a ^ b
print(a, "XOR", b, "=", c)
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)
