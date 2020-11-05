#Question 9 

from math import inf

def dijkstra(origin,destination,visited = None):

    if visited is None:#A l'initialisation, l'ensemble des sommets atteints est vide
        visited = set()
    
    if origin.value == destination: #Si on est arrivé à destination, terminer l'algorithme => return
        return(0, origin.value)
    
    distance = inf
    path = origin.value
    visited.add(origin.value)#Ajoute le point à l'ensemble des sommets visités
    
    for relationship in origin.relationships:
        
        if relationship.value == 99999:
            continue
        
        neighbour = relationship.to #Les voisins atteignables
        
        
        if neighbour.value not in visited:#Si un des voisins n'a pas encore été visités
            distance_temp, path_temp = dijkstra(neighbour, destination, visited) #On se déplace sur ce point et fait l'algo à partir de ce points.
                                                                                 
                
            total_distance = distance_temp + relationship.value #Distance du chemin optimal à partir du neighbor + distance entre le point de départ et le neighbour.
                                                                  
                                                                
                                                                
            if total_distance < distance: #Si le chemin en question est meilleur que les précédents, on le sauvegarde.
                distance = total_distance
                path = origin.value + path_temp 
                
    return (distance, path) 
