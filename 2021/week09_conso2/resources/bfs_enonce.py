# # trouve le chemin le plus court entre 2 noeuds d'un graphe en utilisant BFS
def bfs_shortest_path(graph, start, goal):
        #TODO


if __name__ == '__main__':
    # Exemple de graphe implémenté sous la forme d'un dictionnaire
    graph = {'A': ['B', 'C', 'E'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F', 'G'],
             'D': ['B'],
             'E': ['A', 'B', 'D'],
             'F': ['C'],
             'G': ['C']}
    print(bfs_shortest_path(graph, 'G', 'D'))  # devrait afficher  ['G', 'C', 'A', 'B', 'D']



