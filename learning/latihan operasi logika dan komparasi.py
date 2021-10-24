#latihan=======operasi logika dan komparasi========#
inputuser = float(input(
    "Masukan angka yang bernilai \n lebih dari 0 atau kurang dari 5 \n dan \n lebih dari 8 atau kurang dari 11\n : "))

islebih = (inputuser > 0)
print("lebih dari 3 : ", islebih)

iskurang = (inputuser < 5)
print("kurang dari 5 : ", iskurang)

islebih = (inputuser > 8)
print("lebih dari 8 : ", islebih)

iskurang = (inputuser < 11)
print("kurang dari 11 : ", iskurang)

iscorret = islebih or iskurang and islebih or iskurang
print("angka yang anda masukan : ", iscorret)
