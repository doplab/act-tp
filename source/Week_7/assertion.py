from math import inf
from Graph import Graph

def djikstra(origin, destination, visited = None):
    if visited is None:
        visited = set()
    if origin.value == destination:
        return (0, origin.value)
    distance = inf
    path = origin.value
    visited.add(origin.value)
    for relationship in origin.relationships:
        neighbour = relationship.to
        if neighbour.value not in visited:
            distance_temp, path_temp = djikstra(neighbour, destination, visited)
            total_distance = distance_temp + relationship.value
            if total_distance  < distance:
                distance = total_distance
                path = origin.value + path_temp
    return (distance, path)

def red_print(_input):
    print("\x1b[31m\""+ str(_input) +"\"\x1b[0m")
    
def green_print(_input):
    print("\033[32m\""+ str(_input) +"\"\x1b[0m")
    
def assert_answer(_input, correct):
    correct_answer = False
    if isinstance(correct, set):
        correct_answer = _input in correct
    else:
        correct_answer = _input == correct
    if correct_answer:
        green_print("Bonne réponse!")
    else:
        red_print("Mauvaise réponse, RECU: " + str(_input) + ", ATTENDU: " + str(correct))
        

def graph_eq(graph):
    vertices = [
        [ 0 , 0 , 0 , 0 , 0 ],
        [ 700 , 0 , 0 , 0 , 550 ],
        [ 1300 , 500 , 0 , 0 , 900 ],
        [ 1100 , 850 , 400 , 0 , 1000 ],
        [ 0 , 0 , 0 , 0 , 0]
    ]
    assert_answer(graph, Graph(vertices))

def output_q2():
    vertices = [
        [ 0 , 0 , 0 , 0 , 0 ],
        [ 700 , 0 , 0 , 0 , 550 ],
        [ 1300 , 500 , 0 , 0 , 900 ],
        [ 1100 , 850 , 400 , 0 , 1000 ],
        [ 0 , 0 , 0 , 0 , 0]
    ]
    g = Graph(vertices)
    a = g.get_node("D")
    for relationship in a.relationships:
        print(relationship.to.value, relationship.value)


def assert_djikstra(answer, vertices, origins, destinations):
    g = Graph(vertices)
    print("Data:")
    for vec in vertices:
        print("\t",vec)
    print("\n")
    for o in origins:
        for d in destinations:
            node = g.get_node(o)
            ours = djikstra(node, d)
            theirs = answer(node, d)
            print("Origine: %s, Destination: %s" % (o,d))
            assert_answer(theirs, ours)