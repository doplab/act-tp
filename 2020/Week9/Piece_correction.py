
import numpy as np

#La fonction Piece retourn une liste contenant des 0 et des 1, considérez un 1 comme un succès, i.e. une fois ou la pièce tombe sur pile, et 0 comme un échec
def Piece(l):
    return np.random.randint(0,2,l)



def proba(n,l,iter):
    #Codez , n correspond au nombre de succès et l au nombre d'essaie. Iter correspond au nombre d'expérience que vous allez réaliser pour obtenir la réponse. Cela devrait être grand mais pas trop (sinon le programme prendra trop de temp.)
    #10000 est un bon nombre d'itération.
    proba = 0
    for i in range(iter):
        temp = Piece(l)#On simule une expérience de l lancé.
        count = temp.sum()#On compte le nombre de fois que l'on obtient pile
        if count == n:#Si le nombre de pile obtenue correspond à la probabilité que l'on veut estimer
            proba +=1#On ajoute 1 à notre estimateur de probabilité
            
        
        
    return proba/iter#Divise notre estimateur de probabilité par le nombre total d'expérience réalisée.


n = 5
l = 10
print("La probabilité d'avoir {} pile en  {} lancés de pièce est approximativement égale à {}".format(n,l,proba(n,l,10000)))