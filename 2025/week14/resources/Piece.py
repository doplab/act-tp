import random

# La fonction flip(l) retourne une liste de longueur l contenant des 0 et des 1, considérez un 1 comme un succès, i.e. une fois ou la pièce tombe sur pile, et 0 comme un échec.
def flip(l):
    return [random.randint(0, 1) for i in range(l)]

def proba(n,k,iter):
    # Complétez ici
    
    return None

if __name__ == '__main__':
    n = 10
    k = 5
    print(f"La probabilité d'avoir {k} piles en {n} lancés de pièce est approximativement égale à {proba(n, k, 10000)}")
