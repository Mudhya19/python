# Largest pair sum in array

def largest_pair_sum(numbers):
    list = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                list.append(numbers[i] + numbers[j])
            else:
                list.append(numbers[j] + numbers[i])
    return max(list)
