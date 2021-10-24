num1 = float(input("Masukan angka pertama: "))
op = input("Masukan operator: ")
num2 = float(input("Masukan angka kedua: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Operator syntax error")
