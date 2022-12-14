import random

# lst représente la liste à trier, l l'index 0 et r la taille de la liste -1
def sort(lst, l, r):
        # Dans le meilleur des cas, on arrête la récursivité
        if r <= l:
            return

        # Choix du pivot
        pivot_index = random.randint(l, r)

        # On déplace le pivot au premier élément
        lst[l], lst[pivot_index] = lst[pivot_index], lst[l]

        # partition
        i = l
        for j in range(l+1, r+1):
            if lst[j] < lst[l]:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]

        # On place le pivot à la position adéquate
        lst[i], lst[l] = lst[l], lst[i]

        # On effectue le tri de façon récursive sur les parties gauches et droites de la liste
        sort(lst, l, i-1)
        sort(lst, i+1, r)

def quicksort(items):    
    if items is None or len(items) < 2:
        return
    sort(items, 0, len(items) - 1)

l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
quicksort(l)
print('Liste triée:   ', l)
