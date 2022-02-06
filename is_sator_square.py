tablet = [['K', 'N', 'I', 'T'], ['N', 'O', 'R', 'I'],
          ['I', 'R', '0', 'N'],  ['T', 'I', 'N', 'K']]


def is_sator_square(tablet):
    n = len(tablet)

    lr = ""
    for i in range(n):
        for j in range(n):
            lr += (tablet)[i][j]
    rl = ""
    for i in range(n):
        for j in range(n):
            rl += (tablet)[n-1-i][n-1-j]
    tb = ""
    for i in range(n):
        for j in range(n):
            tb += (tablet)[j][i]
    bt = ""
    for i in range(n):
        for j in range(n):
            bt += (tablet)[n-1-j][n-1-i]
    lr != rl
    tb != bt
    return lr == rl == tb == bt
