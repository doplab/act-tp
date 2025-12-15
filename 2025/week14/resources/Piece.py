import random

# La fonction Piece retourne une liste contenant des 0 et des 1, considérez un 1 comme un succès, i.e. une fois ou la pièce tombe sur pile, et 0 comme un échec
def piece(k):
    return [random.randint(0, 1) for i in range(k)]

def proba(n,k,iter):
    #CODEZ ICI
    
    return None


n = 5
l = 10
print("La probabilité d'avoir {} piles en {} lancés de pièce est approximativement égale à {}".format(n, l, proba(n, l,10000)))
