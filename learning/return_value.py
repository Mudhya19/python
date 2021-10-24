# fungsi dengan return value
def kuadrat(jumlah):
    total = jumlah**2
    print("Nilai kuadrat dari ", jumlah, "ditemukan", total)
    return total


a = kuadrat(5)
print(a)

print(45*"=")


def arguments(argument1, argument2):
    total = argument1 + argument2
    print(argument1, "+", argument2, "=", total)
    return total


a = arguments(2, 9)
print(a)
