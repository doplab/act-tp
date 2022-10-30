# n un nombre entier
def algo3(n):
    i = 1
    s = 0
    while i < n:
        s += i
        i *= 2
    return s
