# https://www.codewars.com/kata/59b11f57f322e5da45000254/train/python

# print(ones_complement('1101'))
# print(ones_complement('1111'))
# print(ones_complement('1010'))
# print(ones_complement('1011'))
# print(ones_complement('1001'))
# print(ones_complement('1000'))
# print(ones_complement('0101'))
# print(ones_complement('0111'))

# ones_complement(1001) = 0110
# ones_complement(1001) = 0110


def ones_complement(binary_number):
    # your code here
    binary_number = binary_number[::-1]
    for i in range(len(binary_number)):
        if binary_number[i] == '0':
            binary_number = binary_number[:i] + '1' + binary_number[i+1:]
        else:
            binary_number = binary_number[:i] + '0' + binary_number[i+1:]
    return binary_number[::-1]
