def factoriel(n):
        if n == 1:
            return n
        else:
            return n * factoriel(n - 1)

#Exécution de la fonction
factorielle(4)
#La fonction retourne 24
