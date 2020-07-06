# Exercice 9
def pair(l):
    return {x: x % 2 == 0 for x in l}

print(pair([1, 4, 3, 7, 8]))
# La fonction pair genère un dictionnaire avec pour clé i (issu de la liste l) et pour valeur le résultat de la fonction estPair définie à la question 2.
