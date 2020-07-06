# Exercice 3
def multiplicateur(n):
    return lambda x: x * n

print (multiplicateur(2)(3))
# La fonction multiplicateur prend en entrée un entier (n) et renvoie une fonction anonyme qui prend en entrée un entier (n) et l'associe à n
