# trouve le chemin le plus court entre 2 noeuds d'un graphe en utilisant BFS
def bfs_shortest_path(graph, start, goal):
    # garder une trace des noeuds visites
    visited = []
    # garder une trace de tous les chemins à vérifier
    queue = [[start]]

    # retourner le chemin si le noeud de départ est celui d'arrivée
    if start == goal:
        return "start = goal"

    # continue de boucler jusqu'à ce que tous les chemins possibles aient été vérifiés
    while len(queue)>0:
        # extraire le premier chemin de la file d'attente
        path = queue.pop(0)
        # récupérer le dernier noeud du chemin
        node = path[-1]
        if node not in visited:
            neighbours = graph[node]
            # parcourir tous les noeuds voisins, construire un nouveau chemin et
            # le mettre dans la file d'attente
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # retourner le path si le voisin est le noeud d'arrivée
                if neighbour == goal:
                    return new_path

            # marquer le noeud comme visité
            visited.append(node)

    # au cas où il n'y aurait pas de chemin entre les 2 noeuds
    return "il n'y a pas de chemin reliant les deux noeuds"




if __name__ == '__main__':
    # Exemple de graphe sous forme de dictionnaire
    graph = {'A': ['B', 'C', 'E'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F', 'G'],
             'D': ['B'],
             'E': ['A', 'B', 'D'],
             'F': ['C'],
             'G': ['C']}
    print(bfs_shortest_path(graph, 'G', 'D'))  # returns ['G', 'C', 'A', 'B', 'D']



