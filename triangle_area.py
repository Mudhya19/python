t_area = {'\n.\n. .\n. . .\n. . . .\n. . . . .\n. . . . . .\n. . . . . . .\n. . . . . . . .\n. . . . . . . . .\n'}


def t_area(a):
    cut = a.split("\n")
    cal = cut[-2].count(' ')
    return ((cal*cal)/2)
