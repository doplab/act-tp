import random

def inside(point):#Point définit sous la forme d'un tuple
    
    if (point[0]**2+point[1]**2) < 1:
        return 1
    
    else: 
        return 0
    
def app():
    count = 0 #On initialise le nombre de point dans le cercle
    for i in range(10000):
        temp1 = random.random()#Génére la première coordonnée
        temp2 = random.random()#Génère la dexuième coordonnée
        temp = [temp1,temp2]#Crée le point

        count += inside(temp)#On appelle la fonction. Si le point est dans le cercle, elle retourn 1, par conséquent on ajoute 1 au compteur. Sinon elle retourne 0, on ajoute donc rien.
    
    return count/10000*4#Retourn selon la formule.

print("L'approximation du chiffre pi est : {}".format(app()))