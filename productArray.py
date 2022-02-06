from functools import reduce


def productArray(numbers):
    result = []
    for i in range(len(numbers)):
        result.append(reduce(lambda x, y: x * y,))
        result = numbers[:i] + numbers[i + 1:]
    return result
