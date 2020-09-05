# Série d'exercice 4: Iteration and recursion 

## Exercice 1: L'itération

Quelques rappels de concepts théorique: 

* L'itération est le procédé répétitif qui boucle jusqu'à ce qu'une condition particulière soit remplie. 
* Il y a deux type de boucle qui sont majoritairement utilisées:
  
  1. **Boucle for**: Les boucles for en python permettent de passer sur tous les éléments d’une liste pour leur appliquer
du code de votre conception. La syntax est la suivante:
On écrit for suivi d’un **nom de variable** de votre choix, suivi du mot-clef **in** et enfin le **nom de
la liste** sur laquelle vous voulez appliquer la boucle. La variable prendra la valeur de chaque
élément dans la liste, un par un. 

   2. **Boucle while**: Les boucles while sont des boucles qui s’exécutent plein de fois d’affilée jusqu’à ce qu’une condition
soit accomplie (une booléenne True ou False). La syntax est la suivante:
On écrit d’abord while, suivi de la condition à atteindre. 


**Note**: 
  * La fonction range(n) permet de créer une liste de nombres de 0 à la valeur passée en argument (n). Lorsqu’elle est combinée à une boucle for, on peut itérer sur une liste de nombres de 0 à n-1.
  * Si vous avez fait une erreur dans votre code, il se peut que la boucle while n’arrive jamais à sa condition
et qu’elle ne se termine donc jamais. Ceci peut entraîner un crash de votre programme, voire
même de votre ordinateur. Il faut donc toujours faire attention à la condition de sortie de la boucle while.


**Question 1: Utilisation de la fonction range() dans une boucle for ( 5 min)**

En utilisant la fonction range() et une boucle for calculez la somme des entier de 0 a 20 et affichez la.

**Hint:** Lorsque range(n) est combinée à une boucle for, on peut itérer sur une liste de nombres de 0 à n-1

**Solution:**

```Python
    somme = 0
    for i in range(21):
        somme += i   #A chaque itération on rajoute i à somme. 
    print(somme)
     
 ```

