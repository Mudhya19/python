#========= operasi logika dan komparasi ============#
inputuser = float(input(
    "Masukan angka yang bernilai : \n kurang dari 3 \n atau \n lebih dari 10 \n : "))


islebih = (inputuser < 3)
print("Lebih dari 3 = ", islebih)

iskurang = (inputuser > 10)
print("kurang dari 10 = ", iskurang)

iscorret = islebih or iskurang
print("angka yang anda masukan : ", iscorret)

# kasus irisan
inputuser = float(input(
    "Masukan angka yang bernilai: \n kurang dari 3 \n atau \n lebih dari 10 \n : "))

islebih = (inputuser < 3)
print("Lebih dari 3 = ", islebih)

iskurang = (inputuser > 10)
print("kurang dari 10 = ", iskurang)

iscorret = islebih and iskurang
print("angka yang anda masukan : ", iscorret)
