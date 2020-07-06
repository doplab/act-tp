# Exercice 10
villes = {'Zurich': 409241, 'Genève': 200548, 'Bâle': 171513, 'Lausanne': 138905, 'Berne': 133798}
print(reduce(lambda x, y: x + y, villes.values()) / len(villes))
# Reduce réduit les résultats de la fonction anonyme qui prend 2 paramètres issus de 'villes.values'. Le résultat final est ensuite divisé par la taille du dictionnaire 'villes' trouvé en utilisant la fonction len()
