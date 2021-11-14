# # trouve le chemin le plus court entre 2 noeuds d'un graphe en utilisant BFS
def bfs_shortest_path(graph, start, goal):
        #TODO


if __name__ == '__main__':
    # sample graph implemented as a dictionary
    graph = {'A': ['B', 'C', 'E'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F', 'G'],
             'D': ['B'],
             'E': ['A', 'B', 'D'],
             'F': ['C'],
             'G': ['C']}
    print(bfs_shortest_path(graph, 'G', 'D'))  # prints  ['G', 'C', 'A', 'B', 'D']



