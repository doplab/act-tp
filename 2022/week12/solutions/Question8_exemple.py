#Question 8

A = graphe.get_node('A')
Arete_liee_noeud_A = A.relationships #Cette variable continent une liste d'arêtes

print("Le nombre d'arêtes liées à A est : {}.".format(len(Arete_liee_noeud_A)))

# Vous pouvez voir que le sommet A est bien lié à 7 autres sommets. (Pour rappel, le sommet A est virtuellement
#lié à 7 sommets dans la matrice d'adjacence)

vertice = Arete_liee_noeud_A[1] #On sélectionne la 2ème arête liée au sommet A (pour rappel les indices d'une liste Python commence à 0)

# Pour déterminer d'où vient l'arête et où elle se termine, utilisez .to.value et _from.value :
print("L'arête part du point : {}".format(vertice._from.value))
print("Et arrive au point : {}".format(vertice.to.value))

#Pour obtenir le poids de cette arête, faites : vertice.value :
print("Le poids de l'arête est : {}".format(vertice.value))