# Exercice 7
from functools import reduce

produit = lambda x, y: x * y
print(reduce(produit, range(1, 11)))
# La fonction anonyme prend 2 arguments en entrée et retourne leur produit tandis que reduce() prend en argument la fonction 'produit' et une liste (range(1, 11)). Elle réduit la liste à une seule valeur calculée en appliquant successivement 'produit' au résultat intermédiaire et à un élément de la liste.
# Ne pas oublier d'importer reduce à partir du package functools: from functools import reduce
