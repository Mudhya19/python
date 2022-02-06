def even_last(numbers):
    result = 0
    for i in range(len(numbers)):
        if i % 2 == 0:
            result += numbers[i] * numbers[-1]
    return result
