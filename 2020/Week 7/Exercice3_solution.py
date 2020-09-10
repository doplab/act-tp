#Exercice 3

class Graph:
    #Cette partie du code permet de créer un graphe lorsqu'on appelle Graph(), il faut spécifier une matrice d'adjascence
    def __init__(self, connections): 
        length = len(connections)   
        self._nodes = {}
        for column in range(length):
            column_length = len(connections[column])
            if column_length is not length:
                raise ValueError("Length of column %d is not the same as the total length (%d)" % (column, length))
            for row in range(column_length):
                connection_value = connections[column][row]
                if not connection_value:
                    continue
                value1 = chr(column + 65)
                value2 = chr(row + 65)
                n1 = self.add_node(value1)
                n2 = self.add_node(value2)
                self.connect(connection_value, n1, n2)
                
    #Cette fonction permet d'ajouter un sommet à notre graphe
    def add_node(self, value):
        if value not in self._nodes:
            self._nodes[value] = self.Node(value)
        return self._nodes[value]
    
    #Cette fonction permet de connecter 2 sommets par une arrête et de lui donner un poids
    def connect(self, value, node1, node2):
        relationship = self.Relationship(value, node1, node2)
        node1.add_relationship(relationship)

    #Cette fonction permet de récupérer les informations d'un sommet du graphe
    def get_node(self, value):
        if value in self._nodes:
            return self._nodes[value]
        return None
    
    #Les sommets du graphes sont noté par des valeurs (ici, A,B,C,...), cette fonction liste toutes
    #les valeurs apparaissant dans le graphes
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
            
        #Un sommet contient la liste de tout les sommets auxquels il est relié.    
        #Cette fonction permet d'ajouter un sommet à la liste.
        def add_relationship(self, relationship): 
            self.relationships.append(relationship)
            
            
        def __str__(self, visited = set(), depth=0):
            if self.value in visited:
                return "{\"value:\" " + self.value + "}"
            output = "{\"value\": %s, \"relationships\": [" % self.value
            for i in self.relationships:
                output += "\n" 
                for _ in range(depth):
                    output += "\t"
                output += i.to.__str__(visited, depth+1)
            output += "]},"
            visited.add(self.value)
            return output
        
        
        #Donne tout les sommets auquels le sommet un sommet est relié
        def get_relationships(self):
            return set([(rel.to.value, rel.value) for rel in self.relationships])

        def __eq__(self, other):
            if self.value != other.value:
                return False
            if self.get_relationships() != other.get_relationships():
                return False
            return True

    #Une relation, i.e. une arrête, part d'un endroit arrive à un endroit et à un certain poids.
    #Permet de créer une relation.
    class Relationship:
        def __init__(self, value, _from, _to):
            self.value = value
            self._from = _from
            self.to = _to
            
            
#Question 7
i = 99999 #Utilisez cette variable pour représenter les relations entre sommets qui ne sont pas dans le graphe.

Adjascency_matrix = [[0,7,i,i,14,i,i,i ],
                     [i,0,8,i,i,i,i,i  ],
                     [i,i,0,6,i,i,i,i  ],
                     [18,i,i,0,i,11,i,i],
                     [i,i,i,i,0,19,i,i ],
                     [i,i,i,i,i,0,4,13 ],
                     [i,i,5,i,i,i,0,9  ],
                     [i,i,9,i,i,i,i,0  ]]

graphe = Graph(Adjascency_matrix)


###########################################################################################################


#Question 8 : Exemple

A = graphe.get_node('A')
Arrete_liee_noeud_A = A.relationships #Cette variable continent une liste d'arrête
#A ce stade, vous ne savez pas encore comment "lire" ce que contient la variable Arrete_liee_noeud_A

print("Le nombre d'arrête liée à A est : {}.".format(len(Arrete_liee_noeud_A)))

#Cependant, vous pouvez voir que le sommet A est bien lié à 7 autres sommets. (Pour rappel, le sommet A est virtuellement
#lié à 7 sommets dans la matrice d'adjascence)

vertice = Arrete_liee_noeud_A[1] #On sélectionne la 2ème arrête liée au sommet A (pour rappele les indice d'une liste 
#python commence à 0)

#Pour déterminer d'ou vient l'arrête et ou elle se termine, utilisez .to.value et _from.value :
print("L'arrête part du point : {}".format(vertice._from.value))
print("Et arrive au point : {}".format(vertice.to.value))

#Pour obtenir le poids de cette arrête, faites : vertice.value :
print("Le poids de l'arrête est : {}".format(vertice.value))

#Question 8 : Exercice 

def linked(graph,N):
    N = graph.get_node(N)
    
    relationships = N.relationships
    
    for rel in relationships:
        if rel.value == 99999:
            continue
        else : 
            print(rel.to.value, rel.value)
        
    return None

linked(graphe, "D")

#Question 9 : Dijkstra

from math import inf

def dijkstra(origin,destination,visited = None):

    if visited is None:#A l'initialisation, l'ensemble des sommets atteints est vide
        visited = set()
    
    if origin.value == destination: #Si on est arrivé à destination, terminer l'algorithme => return
        return(0, origin.value)
    
    distance = inf
    path = origin.value
    visited.add(origin.value)#Ajoute le point à l'enseble des sommets visités
    
    for relationship in origin.relationships:
        
        if relationship.value == 99999:
            continue
        
        neighbour = relationship.to #Les voisins atteignables
        
        
        if neighbour.value not in visited:#Si un des voisins n'a pas encore été visités
            distance_temp, path_temp = dijkstra(neighbour, destination, visited) #On se déplace sur ce point et fait l'algo
                                                                                 #à partir de ce points.
                
            total_distance = distance_temp + relationship.value #Distance du chemin optimal à partir du neighbor + distance
                                                                #entre le point de départ et le neighbour.  
            if total_distance < distance: #Si le chemin en question est meilleur que les précédents, on le sauvegarde.
                distance = total_distance
                path = origin.value + path_temp 
                
    return (distance, path)


print(dijkstra(graphe.get_node('A'), 'H'))