
def plus_proche_binaire(liste, e):
    low = 0
    high = len(liste) - 1

    if(e >= liste[high]):
        return liste[high]
    if(e <= liste[low]):
        return liste[low]

    while low <= high:  # 0<10 and true puis 6<10 and true, etc.
        mid = (low + high) // 2  # mid = 5 --> 16 in list
        print(mid)
        if e > liste[mid]:  # 41>16
            low = mid + 1  # min = 5+1=6
        elif e < liste[mid]:
            high = mid - 1
        else:
            return liste[mid]

    if abs(liste[low]-e) < abs(liste[high]-e) :
        return liste[low]
    else:
        return liste[high]


if __name__ == '__main__':
    L = [1, 2, 5, 8, 12, 16, 24, 56, 58, 63]
    e = 61
    print(plus_proche_binaire(L, e))

