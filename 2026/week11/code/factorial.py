def factorial(n):
    if n < 0:
        raise ValueError()
    if n == 1 or n == 0:
        return n
    else:
        return n * factorial(n - 1)

# Exécution de la fonction
print(factorial(4)) # Affiche 24
