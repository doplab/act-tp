import random

# La fonction Piece retourne une liste contenant des 0 et des 1, considérez un 1 comme un succès, i.e. une fois ou la pièce tombe sur pile, et 0 comme un échec
def Piece(l):
    return [random.randint(0, 1) for i in range(l)]



def proba(n,l,iter):
    #CODEZ ICI
    
    return None


n = 5
l = 10
print("La probabilité d'avoir {} pile en {} lancés de pièce est approximativement égale à {}".format(n, l, proba(n, l,10000)))
