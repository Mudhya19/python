num1 = float(input("Masukan angka pertama: "))
op = input("Masukan operator: ")
num2 = float(input("Masukan angka kedua: "))
num3 = 0


def calculator(num1, op, num2):
    if op == "+":
        num3 = (num1 + num2)
        return num3
    elif op == "-":
        num3 = (num1 - num2)
        return num3
    elif op == "/":
        num3 = (num1 / num2)
        return num3
    elif op == "*":
        num3 = (num1 * num2)
        return num3
    elif op == "**":
        num3 = (num1 ** num2)
        return num3
    elif op == "%":
        num3 = (num1 % num2)
        return num3
    elif op == "//":
        num3 = (num1 // num2)
        return num3
    else:
        return ("Not a Found")


print(f'{num1}{op}{num2}={num3}')
