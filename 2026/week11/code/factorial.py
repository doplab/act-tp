def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

# Exécution de la fonction
print(factorial(4)) # Affiche 24
