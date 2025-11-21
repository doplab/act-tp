def factoriel(n):
    if n == 1:
        return n
    else:
        return n * factoriel(n - 1)

# Exécution de la fonction
print(factorielle(4)) # Affiche 24
