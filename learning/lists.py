# lists

Data = [1, 4, 9, 16, 25, 36, 49, 64]


# mengakses list
Subdata1 = Data[3]
Subdata2 = Data[-3]

print(Subdata2)

# memotong list
Subdata3 = Data[2:4]
Subdata4 = Data[:4]

# menambah list
Data2 = [100, 200, 300, 400, 500, 600, 700, 800]

Data3 = Data + Data2

# merubah content dari list
Data[4] = 87

# mencopy list ke variabel baru
a = Data[:]
a[7] = 87

# merubah content list dengan menggunakan metode slicing
Data[3:5] = [11, 12]

# list dalam list
x = [Data, Data2]

# mengakses list dalam multidimensional list
y = x[0][3]
print(x)
print(y)

# methods untuk list
Data.append(30)
print(Data)

# function yang bisa kita gunakan kepada list
panjang_list = len(Data)

print(panjang_list)
