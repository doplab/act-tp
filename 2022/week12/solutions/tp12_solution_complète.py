# Exercice 3

class Graph:
    # Cette partie du code permet de créer un graphe lorsqu'on appelle 
Graph(), il faut spécifier une matrice d'adjacence
    def __init__(self, connections):
        if connections is None:
            raise ValueError("Graph cannot be None")
        length = len(connections)
        self._nodes = {}
        for column in range(length):
            column_length = len(connections[column])
            if column_length is not length:
                raise ValueError("Length of column %d is not the same as 
the total length (%d)" % (column, length))
            for row in range(column_length):
                connection_value = connections[column][row]
                if not connection_value:
                    continue
                value1 = chr(column + 65)
                value2 = chr(row + 65)
                n1 = self.add_node(value1)
                n2 = self.add_node(value2)
                self.connect(connection_value, n1, n2)

    # Cette fonction permet d'ajouter un sommet à notre graphe
    def add_node(self, value):
        if value not in self._nodes:
            self._nodes[value] = self.Node(value)
        return self._nodes[value]

    # Cette fonction permet de connecter 2 sommets par une arête et de lui 
donner un poids
    def connect(self, value, node1, node2):
        relationship = self.Relationship(value, node1, node2)
        node1.add_relationship(relationship)

    # Cette fonction permet de récupérer les informations d'un sommet du 
graphe
    def get_node(self, value):
        if value in self._nodes:
            return self._nodes[value]
        return None

    # Les sommets du graphe sont notés par des valeurs (ici, A,B,C,...), 
cette fonction liste toutes
    # les valeurs apparaissant dans le graphe
    def get_values(self):
        return set(self._nodes.keys())

    def __eq__(self, other):
        length = len(self._nodes)
        if length is not len(other._nodes):
            return False
        for key in self._nodes:
            corresponding = other.get_node(key)
            if corresponding != self._nodes[key]:
                return False
        return True

    class Node:
        def __init__(self, value):
            self.value = value
            self.relationships = []

        # Un sommet contient la liste de tous les sommets auxquels il est 
relié.
        # Cette fonction permet d'ajouter un sommet à la liste.
        def add_relationship(self, relationship):
            self.relationships.append(relationship)

        def __str__(self, visited=set(), depth=0):
            if self.value in visited:
                return "{\"value:\" " + self.value + "}"
            output = "{\"value\": %s, \"relationships\": [" % self.value
            for i in self.relationships:
                output += "\n"
                for _ in range(depth):
                    output += "\t"
                output += i.to.__str__(visited, depth + 1)
            output += "]},"
            visited.add(self.value)
            return output

        # Donne tous les sommets auxquels le sommet est relié
        def get_relationships(self):
            return set([(rel.to.value, rel.value) for rel in 
self.relationships])

        def __eq__(self, other):
            if self.value != other.value:
                return False
            if self.get_relationships() != other.get_relationships():
                return False
            return True

    # Une relation, i.e. une arête, part d'un endroit arrive à un endroit 
et a un certain poids.
    # Permet de créer une relation.
    class Relationship:
        def __init__(self, value, _from, _to):
            self.value = value
            self._from = _from
            self.to = _to


# Question 7
i = 99999  # Utilisez cette variable pour représenter les relations entre 
sommets qui ne sont pas dans le graphe.
Adjacency_matrix = None

# Question 7

i = 0
Adjacency_matrix = [[0, 7, i, i, 14, i, i, i],
                    [i, 0, 8, i, i, i, i, i],
                    [i, i, 0, 6, i, i, i, i],
                    [18, i, i, 0, i, 11, i, i],
                    [i, i, i, i, 0, 19, i, i],
                    [i, i, i, i, i, 0, 4, 13],
                    [i, i, 5, i, i, i, 0, 8],
                    [i, i, 9, i, i, i, i, 0]]

graphe = Graph(Adjacency_matrix)

###########################################################################################################


# Question 8 : Exemple

A = graphe.get_node('A')
Arrete_liee_noeud_A = A.relationships  # Cette variable contient une liste 
d'arête
# À ce stade, vous ne savez pas encore comment "lire" ce que contient la 
variable Arrete_liee_noeud_A

print("Le nombre d'arête liée à A est : 
{}.".format(len(Arrete_liee_noeud_A)))

# Cependant, vous pouvez voir que le sommet A est bien lié à 7 autres 
sommets. (Pour rappel, le sommet A est virtuellement
# lié à 7 sommets dans la matrice d'adjascence)

vertice = Arrete_liee_noeud_A[1]  # On sélectionne la 2ème arête liée au 
sommet A (pour rappel les indices d'une liste
# Python commence à 0)

# Pour déterminer d'où vient l'arête et où elle se termine, utilisez 
.to.value et _from.value :
print("L'arête part du point : {}".format(vertice._from.value))
print("Et arrive au point : {}".format(vertice.to.value))

# Pour obtenir le poids de cette arête, faites : vertice.value :
print("Le poids de l'arête est : {}".format(vertice.value))


# Question 8 : Exercice

# Question 8

def linked(graph, N):
    N = graph.get_node(N)  # Accède au nœud N, permet par la suite d'en 
récupérer les infos

    relationships = N.relationships  # Accède à toutes les relations du 
point N

    for rel in relationships:  # Parcourt les relations du point N
        if rel.value == 99999:  # Si le poids est de 99999 il n'y pas de 
relation dans le graphe -> itération suivante
            continue
        else:
            print(rel.to.value, rel.value)  # Sinon on affiche la 
destination, puis le poids de l'arrête.

    return None


linked(graphe, 'D')

# Question 9 - Dijkstra

from math import inf


def dijkstra(origin, destination, visited=None):
    if visited is None:  # A l'initialisation, l'ensemble des sommets 
atteints est vide
        visited = set()

    # Question 9.1
    if origin.value == destination:  # Si on est arrivé à destination, 
terminer l'algorithme => return
        return 0, origin.value

    distance = inf
    path = origin.value
    visited.add(origin.value)  # Ajoute le point à l'ensemble des sommets 
visités

    # Question 9.2
    for relationship in origin.relationships:

        # Question 9.3
        if relationship.value == 99999:
            continue

        neighbour = relationship.to  # Les voisins atteignables

        if neighbour.value not in visited:  # Si un des voisins n'a pas 
encore été visités
            distance_temp, path_temp = dijkstra(neighbour, destination,
                                                visited)  # On se déplace 
sur ce point et fait l'algo à partir de ce points.

            total_distance = distance_temp + relationship.value  # 
Distance du chemin optimal à partir du neighbor + distance entre le point 
de départ et le neighbour.

            # Question 9.4
            if total_distance < distance:  # Si le chemin en question est 
meilleur que les précédents, on le sauvegarde.
                distance = total_distance
                path = origin.value + path_temp

    return distance, path


print(dijkstra(graphe.get_node('A'), 'H'))

