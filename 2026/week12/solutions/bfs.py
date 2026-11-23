# Question 2

adjacency_list_graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

def bfs(graph, start):
    visited = list(start) # liste des sommets visités
    queue = [start] # liste des sommets *dont les voisins* sont à visiter
    order = [] # pour stocker l'ordre de sommets (sommets proches d'abord puis les sommets qui sont plus loin)
    while len(queue) > 0: # tant que la queue n'est pas vide
        u = queue.pop(0) # on stocke le premier élément de la queue, puis on l'enlève de la queue
        order.append(u)
        neighbors = graph[u] # on récupère la liste des sommets adjacents au sommet courant
        for v in neighbors: # Puis on parcourt la liste de ceux-ci
            if v not in visited:
                queue.append(v) # on les ajoute à la queue
                visited.append(v)
    return order # on retourne la liste des sommets visités (=atteignables)


# Vérifions que l'algorithme fonctionne correctement
print(bfs(adjacency_list_graph, 'B'))
print(bfs(adjacency_list_graph, 'A'))