nombres = list(range(11)) # attention: range ne renvoie pas une liste
nombres_pairs = [x for x in nombres if x%2==0]
print(nombres_pairs)