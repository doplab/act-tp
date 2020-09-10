#Question 2

adjacency_list_graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}


def BFS(graphe,s):
    queue = [s] #on initialise la queue
    visited = [s]#on initialisela liste des sommets visités
    
    while len(queue) != 0: #Aussi longtemps que la queue n'est pas vide, répéter l'étape 2
        for i in queue: #On parcourt les éléments de la queue
            for k in graphe[i]:#Pour chaque éléments de la queue, on parcout tout les voisins
                if k not in visited:#Si le voisin n'est pas déjà visité, on l'ajoute à la queue, et on le marque comme visité
                    queue.append(k)
                    visited.append(k)
            queue.remove(i) #Une fois que l'élément de la queue a été parcouru, on le supprime de la queue
            
    return visited #On retourne la liste des sommets visités (=atteignables)

#Vérifions que l'algorithme fonctionne correctement
print(BFS(adjacency_list_graph, 'B'))
print(BFS(adjacency_list_graph, 'A'))