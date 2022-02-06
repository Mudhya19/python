def same_case(a, b):
    upper = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lower = set('abcdefghijklmnopqrstuvwxyz')
    if a.isupper() and b.isupper():
        return True
    elif a.islower() and b.islower():
        return True
    elif a.isupper() and b.islower():
        return False
    elif a.islower() and b.isupper():
        return False
    else:
        return False
