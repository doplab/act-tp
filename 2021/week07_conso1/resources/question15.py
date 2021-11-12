import sys
import traceback

# Complétez le code à partir de la ligne 66

def recherche_arbre(node, value):
    if node == None:
        return False
    
    if node.value == value:
        return True
    if node.value > value:
        return recherche_arbre(node.left,value) 
    else:
        return recherche_arbre(node.right,value) 


################## Générations des arbres en python ####################

class Arbre:
    def __init__(self, *args):
        self.root = Node(args[0])
        for i in range(1, len(args)):
            self.insert(args[i], self.root)

    def insert(self, value, node):
        if node.value == value:
            return
        elif value < node.value:
            if node.left is not None:
                return self.insert(value, node.left)
            new_node = Node(value)
            node.left = new_node
        else:
            if node.right is not None:
                return self.insert(value, node.right)
            new_node = Node(value)
            node.right = new_node

    def __str__(self):
        return str(self.root)


def main():
    a = Arbre([8, 6, 10, 2, 10, 3, 3, 23, 100, 323, 22])
    print(a.root)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return "{value: %d, left: %s, right: %s}" % (self.value, self.left, self.right)

###############################################


tree = Arbre(8, 3, 1, 6, 4, 7, 10, 14, 13)
root = tree.root

liste = [3,6,9,18]

#complétez ici




