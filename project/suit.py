import random

pemain = input(
    "Tentukan pilihanmu: \n 'g' gunting, 'b' batu, 'k' kertas:  "
)

komputer = random.choice(['g', 'b', 'k'])

print("Pilihan pemain: ", pemain)
print("Pilihan komputer: ", komputer)

if (pemain == komputer):
    print("Permainan seri")
elif (pemain == 'k' and komputer == 'b') or (pemain == 'b' and komputer == 'g') or (pemain == 'g' and komputer == 'k'):
    print("pemain menang")
else:
    print("komputer menang")
