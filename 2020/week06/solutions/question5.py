def plus_proche_binaire(liste, n):
    # SOLUTION

    min = 0
    max = len(liste)
    found = False
    while min <= max and not found:  # 0<10 and true puis 6<10 and true, etc.
        mid = (max + min) // 2  # mid = 5 --> 16 in list
        print(mid)
        if n > liste[mid]:  # 41>16
            min = mid + 1  # min = 5+1=6
        elif n < liste[mid]:
            max = mid - 1
        else:
            found = True
    if found:
        return n
    else:
        if abs(liste[mid-1]-n) < abs(liste[mid]-n) :
            return liste[mid-1]
        elif abs(liste[mid+1]-n) < abs(liste[mid]-n) :
            return liste[mid+1]
        else :
            return liste[mid]


L = [1, 2, 5, 8, 12, 16, 24, 56, 58, 63]
e = 41
print(plus_proche_binaire(L, e))

