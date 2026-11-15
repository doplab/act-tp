def tri_bulle(l):
    n = len(l)

    for i in range(n - 1):
        # Les i derniers éléments sont à leur position définitive.
        # j parcourt les indices de 0 à n-i-2 inclus.
        for j in range(n - i - 1):
            # Echanger si l'élément de gauche est supérieur à celui de droite.
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

if __name__ == "__main__":
    l = [1, 2, 4, 3, 1]
    tri_bulle(l)
    print(l)
