inputuser = float(input(
    "Masukan angka yang bernilai \n kurang dari 0 atau lebih dari 5 \n dan \n kurang dari 8 atau lebih dari 11 \n :"))

iskurang = (inputuser < 0)
print("kurang dari 0 : ", iskurang)

islebih = (inputuser > 5)
print("lebih dari 5 : ", islebih)

iskurang = (inputuser < 8)
print("kurang dari 8 : ", iskurang)

islebih = (inputuser > 11)
print("lebih dari 11 : ", islebih)

iscorret = iskurang or islebih and iskurang or islebih
print("angka yang anda masukan : ", iscorret)
