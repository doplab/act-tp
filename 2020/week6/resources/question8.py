import sys
import traceback


def recherche_arbre(node, value):
    #Complétez ici





    



################## Ne pas modifier le code ci-dessous ##################


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



################## Test de vérification du code ##################

def handle_error(): #Fonction appelée dans le bloc "except" qui gère les erreurs
    _, _, tb = sys.exc_info()
    traceback.print_tb(tb) 
    tb_info = traceback.extract_tb(tb)
    filename, line, func, text = tb_info[-1]
    print('Une erreur s\'est produite sur la ligne {} dans la déclaration {}'.format(line, text))

try: #"try" permet de tester le code pour détecter les erreurs.

    tree = Arbre(8, 3, 1, 6, 4, 7, 10, 14, 13)
    root = tree.root
    assert recherche_arbre(root, 4) == True # devrait trouver
    assert recherche_arbre(root, 7) == True # devrait trouver
    assert recherche_arbre(root, 18) == False # ne devrait pas trouver
    assert recherche_arbre(root, 21) == False # ne devrait pas trouver

    print("Bonne réponse avec le premier arbre")
except AssertionError: #"except" permet de gérer l'erreur
    handle_error()
    print("Mauvaise réponse")
    
try:
    tree = Arbre(1, 3, 9, 6, 14, -17, 110, 124, 13, -1, 9, 1, 40, -98, 120, 23)
    root = tree.root
    assert recherche_arbre(root, 14) == True # devrait trouver
    assert recherche_arbre(root, 110) == True # devrait trouver
    assert recherche_arbre(root, 39) == False # ne devrait pas trouver
    assert recherche_arbre(root, 18) == False # ne devrait pas trouver
    print("Bonne réponse avec le deuxième arbre")
except AssertionError as err:
    handle_error()
    print("Mauvaise réponse")