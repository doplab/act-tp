class Graph:
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

    def add_node(self, value):
        if value not in self._nodes:
            self._nodes[value] = self.Node(value)
        return self._nodes[value]

    def connect(self, value, node1, node2):
        relationship = self.Relationship(value, node1, node2)
        node1.add_relationship(relationship)

    def get_node(self, value):
        if value in self._nodes:
            return self._nodes[value]
        return None

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

        def get_relationships(self):
            return set([(rel.to.value, rel.value) for rel in self.relationships])

        def __eq__(self, other):
            if self.value != other.value:
                return False
            if self.get_relationships() != other.get_relationships():
                return False
            return True


    class Relationship:
        def __init__(self, value, _from, _to):
            self.value = value
            self._from = _from
            self.to = _to
