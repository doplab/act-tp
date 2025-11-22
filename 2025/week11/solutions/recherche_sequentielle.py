# Définition de la fonction
def recherche_sequentielle(liste, e):
    for idx in range(len(liste)):  # idx représente l'index
        if liste[idx] == e:
            return idx

    return -1

# Solution alternative 
def recherche_sequentielle_while(liste, e):
    i = 0
    while i < len(liste):
        if liste[i] == e:
            return i
        i += 1
    return -1

if __name__ == '__main__':
    L = [123, 321, 328, 472, 549, 328]
    e = 328
    resultat = recherche_sequentielle(L, e)
    print(resultat)  # Affiche 2