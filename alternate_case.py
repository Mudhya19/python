def alternate_case(s):
    for i in range(len(s)):
        if i % 2 == 0:
            s = s[:i] + s[i].upper() + s[i+1:]
        else:
            s = s[:i] + s[i].lower() + s[i+1:]
    return s
