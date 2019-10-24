def df_search(node, value):
    if node.value == value:
        return node
    for child in node.children:
        return df_search(child, value)
    return None