# Exercice 8
from functools import reduce

factorielle = lambda n: reduce(lambda x, y: x * y, range(1, n + 1), 1)
print(factorielle(10)) # test avec 10!
# La fonction reduce prend pour argument une fonction anonyme ('lambda x, y: x * y' qui prend 2 arguments en entrée et retourne leur produit) et une liste l (dans cet exercice, la liste l est générée par 'range(1, n + 1)'). La fonction reduce réduit la liste à une seule valeur calculée en appliquant la fonction anonyme au résultat intermédiaire et à un élément de la liste générée. Le troisième paramètre de reduce est optionel, il s'agit d'une valeur d'initialisation et est passé avec le premier élément de la liste (au lieu que le premier soit passé avec le deuxième) au début de l'exécution. On peut ainsi gérer le cas ou une liste vide serait utilisée (pour calculer la factorielle de 0 par exemple).
