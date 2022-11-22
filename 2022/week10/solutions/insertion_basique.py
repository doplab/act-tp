def insertion_entier(liste, n):
    # On ajoute n à la liste
    liste.append(n)
    for i in range(1, len(liste)):
        key = liste[i]
        j = i - 1
        while j >= 0 and key < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = key
    return liste


print(insertion_entier([2, 4, 6, 4, 7], 1))