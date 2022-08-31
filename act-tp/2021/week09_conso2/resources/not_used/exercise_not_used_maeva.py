def min_max(liste):
    if len(liste) == 1:
        return int(liste[0]), int(liste[0])
    else:
        l1 = min_max(liste[:len(liste)//2])
        l2 = min_max(liste[len(liste)//2:])
        return min(l1[0], l2[0]), max(l1[1], l2[1])

print(min_max(['1', '9', '15']))
