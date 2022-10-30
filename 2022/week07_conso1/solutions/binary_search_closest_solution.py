def recherche_binaire_recursive(L, s, r, e): #fonction 1, recherche binaire
    if s<=r :
        mid = int((s + r) / 2)
        if L[mid] == e:
            return mid
        elif L[mid] > e:
            return recherche_binaire_recursive(L, s, mid - 1, e)
        else:
            return recherche_binaire_recursive(L, mid + 1, r, e)
    else :
        mid = int((s + r) / 2)
        return mid

def plus_proche(L,e,v): #fonction 2, comparaison pour trouver l'élément le plus proche
    
    if v == len(L)-1 : # si l'élément retourné par la première fonction est le dernier élément de la liste, 
        if abs(L[v - 1] - e) < abs(L[v] - e):  # il n'a pas besoin de comparer avec l'élément suivant
            return L[v - 1]
        else :
            return L[v]

    elif v == 0 : # si l'élément retourné par la première fonction est le premier élément de la liste, 
        if abs(L[v + 1] - e) < abs(L[v] - e):  # il n'a pas besoin de comparer avec l'élément d'avant
            return L[v + 1]
        else :
            return L[v]

    else : # cas normal
    	if abs(L[v - 1] - e) < abs(L[v] - e): 
            return L[v - 1]
    	elif abs(L[v + 1] - e) < abs(L[v] - e):
            return L[v + 1]
    	else:
            return L[v]

L = [1, 2, 5, 8, 12, 16, 24, 56, 58, 63]
s = 0
r = len(L)-1
e = 68
print(recherche_binaire_recursive(L, s, r, e))
print(plus_proche(L, e, recherche_binaire_recursive(L, s, r, e)))