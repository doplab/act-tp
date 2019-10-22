def tree_search(node, value):
    if value == node.value:
        return True
    elif value < node.value:
        if node.left:
            return tree_search(node.left, value)
        return False
    else:
        if node.right:
            return tree_search(node.right, value)
        return False