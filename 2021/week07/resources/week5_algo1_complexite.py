import math

# L est une liste d'entiers et x est un nombre entier
def algo1(L, x):
    n = len(L)
    
    for i in range(n):
        L[i] = L[i] + math.pow(x, i)