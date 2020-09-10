#Question 8

A = graphe.get_node('A')
Arrete_liee_noeud_A = A.relationships #Cette variable continent une liste d'arrête
#A ce stade, vous ne savez pas encore comment "lire" ce que contient la variable Arrete_liee_noeud_A

print("Le nombre d'arrête liée à A est : {}.".format(len(Arrete_liee_noeud_A)))

#Cependant, vous pouvez voir que le sommet A est bien lié à 7 autres sommets. (Pour rappel, le sommet A est virtuellement
#lié à 7 sommets dans la matrice d'adjascence)

vertice = Arrete_liee_noeud_A[1] #On sélectionne la 2ème arrête liée au sommet A (pour rappele les indice d'une liste 
#python commence à 0)

#Pour déterminer d'ou vient l'arrête et ou elle se termine, utilisez .to.value et _from.value :
print("L'arrête part du point : {}".format(vertice._from.value))
print("Et arrive au point : {}".format(vertice.to.value))

#Pour obtenir le poids de cette arrête, faites : vertice.value :
print("Le poids de l'arrête est : {}".format(vertice.value))