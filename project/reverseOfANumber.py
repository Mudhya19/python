number = 1234
remainder = []
while number != 0:
    remainder.append(number % 10)
    number //= 10
print("".join(map(str, remainder)))
