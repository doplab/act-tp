# Question 8

def linked(graph,N):
    N = graph.get_node(N)#Accède au noeud N, permet par la suite d'en récupérer les infos
    
    relationships = N.relationships #Accède à toutes les relations du point N
    
    for rel in relationships:#Parcout les relations du point N
        if rel.value == 99999:#Si le poids est de 99999 il n'y pas de relation dans le graphe -> itération suivante
            continue
        else : 
            print(rel.to.value, rel.value)#Sinon on imprime la destination, puis le poids de l'arrête.
        
    return None
