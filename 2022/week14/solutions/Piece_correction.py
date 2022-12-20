import random


# La fonction Piece retourne une liste contenant des 0 et des 1, considérez un 1 comme un succès, i.e. une fois où la pièce tombe sur pile, et 0 comme un échec
def Piece(l):
    return [random.randint(0, 1) for i in range(l)]


def proba(n, l, iter=10000):
    # n correspond au nombre de succès et l au nombre d'essais. Iter correspond au nombre d'expérience que vous allez
    # réaliser pour obtenir la réponse. Cela devrait être grand mais pas trop (sinon le programme prendra trop de
    # temps à s'exécuter). 10000 est un bon nombre d'itérations.
    occurences = 0
    for i in range(iter):
        temp = Piece(l)  # On simule une expérience de l lancés.
        count = sum(temp)  # On compte le nombre de fois que l'on obtient pile
        if count == n:  # Si le nombre de pile obtenu correspond à la probabilité que l'on veut estimer
            occurences += 1  # On ajoute 1 à notre estimateur de probabilité
    return occurences / iter  # Divise notre estimateur de probabilité par le nombre total d'expériences réalisées.


n = 5
l = 10
print("La probabilité d'avoir {} pile en {} lancers de pièce est approximativement égale à {}".format(n, l, proba(n, l,10000)))
