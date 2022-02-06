# simple_remove_duplicates.py


def solve(arr):
    list = arr.copy()
    for i in list:
        if list.count(i) > 1:
            list.remove(i)
        else:
            list.reverse(i)
    return list


def solve(arr):
    re = []
    for i in arr[::-1]:
        if i not in re:
            re.append(i)
    return re[::-1]
