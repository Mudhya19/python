# How Green Is My Valley?

def make_valley(arr):
    sort = sorted(arr)
    odd = len(arr) % 2
    return sort[::2] + sort[odd::-2]
