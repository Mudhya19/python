def symmetric_point(p, q):
    x1 = p[0]
    y1 = p[1]
    x2 = q[0]
    y2 = q[1]
    if x1 == x2:
        return (x1, y1)
    elif y1 == y2:
        return (x1, y1)
    else:
        return (x2, y2)
