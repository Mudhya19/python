nilai = 60

if nilai == 75:  # equal eksplisit
    print("Nilai anda: ", nilai)

if nilai is 60:  # equal
    print("Nilai anda: ", nilai)

if nilai is not 60:  # not equal
    print("Nilai anda: ", nilai)

print(25*"=")

nilai = 70

if 80 <= nilai <= 100:  # jika nilai ada maka akan terouput
    print("nilai anda adalah A ")
elif 70 <= nilai <= 80:  # jika nilai ada di elif akan terouput
    print("nilai anda adalah B ")
elif 60 <= nilai <= 70:
    print("nilai anda adalah C ")
elif 50 <= nilai <= 60:
    print("nilai anda adalah D, Lakukan perbaikan!!!")
else:  # selain nilai if dan elif maka akan terouput dielse
    print("maaf anda tidak lulus mata kuliah ini")

print(25*"+")
print("operator logika untuk list dan string")
print(" ")

gorengan = ["bakwan", "cireng", "bala-bala", "gehu",
            "combro", "pisang goreng", "pukis", "risoles"]
beli = "zimbawe"

if beli in gorengan:
    print('Mamang bilang, " ya, jual ', beli, '"')

if not beli in gorengan:
    print('"saya gak jual', beli, '"')

karakter = "z"
if karakter in beli:
    print("ada", karakter, "di", beli)
else:
    print("tidak ada ", karakter, "di", beli)
