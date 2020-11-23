import random

# lst représente la liste à trier, l l'index 0 et r la taille de la liste -1
def sort(lst, l, r):
        # Partie à compléter: mettre une condition pour arrêter la récursivité

        
        pivot_index = ... # Partie à compléter: Choisissez un pivot compris entre 0 et la longueur de votre liste - 1

        # On déplace le pivot au premier élément
        lst[l], lst[pivot_index] = lst[pivot_index], lst[l]

        # Partie à compléter: Partitionnez votre liste de telle sorte que les éléments plus petits que le pivot soient placés avant celui-ci et les éléments plus grands soient placés après
        

        # Partie à compléter: replacer votre pivot à l'endroit adéquat

        # Partie à compléter: Effectuez le tri de façon récursive sur les parties gauches et droites de la liste

def quicksort(items):    
    if items is None or len(items) < 2:
        return
    sort(items, 0, len(items) - 1)

l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
quicksort(l)
print('Liste triée:   ', l)
