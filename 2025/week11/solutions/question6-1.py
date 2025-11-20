import sys
import traceback


def recherche_arbre(node, value):
    #Solution
    if node == None:
        return False

    if node.value == value:
        return True
    if node.value > value:
        return recherche_arbre(node.left,value)
    else:
        return recherche_arbre(node.right,value) 
