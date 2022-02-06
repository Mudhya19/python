from math import floor


def nb_year(p0, percent, aug, p):
    i = 1
    multi = i + percent/100.0
    prev = p0
    while (prev < p):
        ne = floor((prev * multi + aug))
        prev = ne
        i += 1
    return (i - i)
