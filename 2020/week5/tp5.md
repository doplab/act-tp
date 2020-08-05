# Algorithmes et complexité


## Tri par insertion

Compléter le code suivant pour trier la liste `l` définie ci-dessous en utilisant un tri par fusion.
Combien d'itérations effectuez-vous?
```Python

def tri_insertion(l):
    for i in range(1, len(l)):
        #TODO: Code à compléter

if __name__ == "__main__":
    l = [2, 43, 1, 3, 43]
    liste_triee = tri_insertion(l)
    print(liste_triee)
```

## Tri à bulles

Le tri à bulles consiste à parcourir une liste et à comparer ses éléments. Le tri est effectué en permutant les éléments de telle sorte que les éléments les plus grands soient placés à la fin de la liste.

Soit la liste `l` suivante, trier les éléments de la liste suivante en utilisant un tri à bulles. Combien d'itération effectuez-vous?

```Python

def tri_bulle(l):
    for i in range(1, len(l)):
        #TODO: Code à compléter

if __name__ == "__main__":
    l = [1, 2, 4, 3, 1]
    liste_triee = tri_bulle(l)
    print(liste_triee)

```


## Tri fusion