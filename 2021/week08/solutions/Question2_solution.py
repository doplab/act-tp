#Question 2

adjacency_list_graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

def BFS(graph, start):
    visited = list() # liste des sommets visités
    queue = [start] # liste des sommets à visiter
    while len(queue) > 0: # tant que la queue n'est pas vide
        node = queue.pop(0) # on stocke le premier élément de la queue, puis on l'enlève de la queue
        if node not in visited: # si le sommet n'a pas déjà été visité
            visited.append(node) # on l'ajoute à la liste des sommets visités
            neighbors = graph[node] # on récupère la liste des sommets adjacents au sommet courant
        for neighbor in neighbors: # Puis on parcourt la liste de ceux-ci
            queue.append(neighbor) # on les ajoute à la queue
    return visited # on retourne la liste des sommets visités (=atteignables)


# Vérifions que l'algorithme fonctionne correctement
print(BFS(adjacency_list_graph, 'B'))
print(BFS(adjacency_list_graph, 'A'))