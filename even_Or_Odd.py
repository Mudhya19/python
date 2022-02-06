# Odd or Even? Determine that!Odd or Even? Determine that!

def even_or_odd(n):
    if n % 2 == 0:
        return "Either"
    elif n % 4 == 0:
        return "Even"
    return "Odd"
