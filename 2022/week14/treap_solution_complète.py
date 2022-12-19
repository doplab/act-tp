import random

random.seed(2)


class TreapNode(object):
    def __init__(self, key, priority, data):
        self.key = key
        self.priority = priority
        self.size = 1
        self.cnt = 1
        self.data = data
        self.left = None
        self.right = None

    def left_rotate(self):
        a = self
        b = a.right
        a.right = b.left
        b.left = a
        a = b
        b = a.left
        b.size = b.left_size() + b.right_size() + b.cnt
        a.size = a.left_size() + a.right_size() + a.cnt
        return a

    def right_rotate(self):
        a = self
        b = a.left
        a.left = b.right
        b.right = a
        a = b
        b = a.right
        b.size = b.left_size() + b.right_size() + b.cnt
        a.size = a.left_size() + a.right_size() + a.cnt
        return a

    def left_size(self):
        return 0 if self.left is None else self.left.size

    def right_size(self):
        return 0 if self.right is None else self.right.size

    def __repr__(self):
        return '[(%s,%s), %s, %s]' % (
            str(self.key), self.priority, str(self.left), str(self.right))


class Treap(object):
    def __init__(self):
        self.root = None

    def _insert(self, node, key, priority, data=None):
        if node is None:
            node = TreapNode(key, priority, data)
            return node
        node.size += 1
        if key < node.key:
            node.left = self._insert(node.left, key, priority, data)
            if node.left.priority > node.priority:
                node = node.right_rotate()
        elif key >= node.key:
            node.right = self._insert(node.right, key, priority, data)
            if node.right.priority > node.priority:
                node = node.left_rotate()

        return node

    def insert(self, key, priority, data=None):
        self.root = self._insert(self.root, key, priority, data)

    def size(self):
        return 0 if self.root is None else self.root.size

    def __repr__(self):
        return str(self.root)


if __name__ == '__main__':
    root = None
    treap = Treap()

    liste = [5, 2, 1, 4, 9, 8, 10]
    nodes = []

    # Création de la liste de noeuds + priorités
    for i in liste:
        pair = (i, random.randrange(100))
        nodes.append(pair)

    print(f"Noeuds avant insertion: {nodes}")

    # Construction de la treap
    for j in nodes:
        treap.insert(j[0], j[1], root)

    print(f"Treap: {treap}")