def descendingOrder(n):
    list = []
    for i in str(n):
        list.append(i)
    list.sort(reverse=True)
    return int(''.join(list))
