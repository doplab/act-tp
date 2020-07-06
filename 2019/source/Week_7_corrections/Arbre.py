class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        output = "{value: %s, children: [" % self.value
        for child in self.children:
            output += str(child)
        output += "]}"
        return output

    def __eq__(self, other):
        if self.value != other.value:
            return False
        length = len(self.children)
        if length != len(other.children):
            return False
        for i in range(length):
            if self.children[i] != other.children[i]:
                return False
        return True

class Arbre:
    def __init__(self, value="root"):
        self.root = Node(value)

    def __eq__(self, other):
        return self.root == other.root

    def __str__(self):
        return str(self.root)


def main():
    a = Arbre([8, 6, 10, 2, 10, 3, 3, 23, 100, 323, 22])
    print(a.root)

if __name__ == "__main__":
    main()