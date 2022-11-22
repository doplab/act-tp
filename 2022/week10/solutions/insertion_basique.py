def insertion_entier(liste, number):
    # ajoute un élément à la liste
    liste.append(number)
    n = len(liste) - 1
    while n > 0 and liste[n - 1] > number:
        liste[n] = liste[n - 1]
        n -= 1
    liste[n] = number
    return liste 


print(insertion_entier([2, 4, 6], 1))
