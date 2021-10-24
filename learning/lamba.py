def jumlah(a, b):
    c = a+b
    return c


hasil = jumlah(4, 5)
print(hasil)

# membuat anonymous function dengan lambda


def kali(argumen): return print(argumen)


kali("test")


def kali(x, y): return x*y


hasil = kali(3, 4)
print(hasil)
