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

**Attention:** Toutes les réponses devront être écrites en python.

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
**Question 2: Création d'une liste à partir d'un tuple ( 5 min)**

Transformer le tuple (1,4,5,8) en une liste à l'aide d'une boucle for.

**Hint:** Rajouter un à un les éléments du tuple dans la liste.

**Solution:**

```Python
    liste_finale = []
    tuple_initial = (1, 4, 5, 8)
    for valeur in tuple_initial:      # A chaque itération valeur est une copie d'un élément du tuple. La boucle se finie au dernier élément du tuple_initial.
        liste_finale.append(valeur)   # On ajoute valeur à la liste crée en dehors de la boucle.
    
     
 ```

**Question 3: Boucle While et input() ( 15 minutes)**
   
   A l'aide d'une boucle while, demander à l'utilisateur de rentrer une valeur. Tant que cette valeur ne correspond pas à 10, le programme redemande à l'utilisateur une valeur.
   
  **Hint:** 
   1. Définir à l'extérieur de la boucle le booléen utilisé pour le test dans while.
    
   2. La fonction input() ressort un string ( chaîne de caractères), il faut changer son type. 
  
  **Solution:**
  
  ```Python
        bool_test = True
        while bool_test:                                          # Tant que bool_test est True, la boucle continue
            test_value = int(input("Veuillez entrer un entier"))  # Pour que le test effectué à la ligne suivante ne soit pas toujours juste                         
                                                                  #  ( comparaison entre un string et un entier), il faut changer le type de l'input.
            bool_test = not(test_value == 10)                     # On veut sortir de la boucle si la test_value est 10. Pour sortir il faut que bool_test soit  
            if bool_test == True:                                 # False. D'où l'utilisation de not qui transforme true en false et vice verse.
                print("Ce n'est pas le bon entier.")              
        print("Bravo !")
  ```
  
  **Question 4: Boucle While et des étudiants ( 15 minutes)**
  
   Considérons une liste d'étudiants contenant le nom de l'étudiant puis si il était en classe ou non. 
   
   l = ["Schmitt", True, "Irma", False, "Khalif", True, "Yasser", False, "Wang", True]
   
   A partir de cette liste et du type de boucle de votre choix créez un dictionnaire ayant pour clés les noms et comme valeur la présence au cours.
   
   **Hint:** 
   
   * i % 2: sort le reste de i par la division euclidienne de 2. ( i % 2 == 0 ) Indique si i est pair.
   
   * Boucle for: Utiliser les indices pour accéder aux éléments de la liste et donc ne pas itérer directement sur les éléments de la liste.
   
   * Boucle while: La condition de sortie devrait être en rapport avec la longueur de la liste.
   
   **Solution:**
   
   Solution avec boucle for:
   
   ```Python
       l = ["Schmitt", True, "Irma", False, "Khalif", True, "Yasser", False, "Wang", True]
       dict_final = {}
       for i in range(len(l)):               # i va de 0 à 9
           if i % 2 == 0:                    # Test si i est pair. Si oui, on crée une nouvelle entrée dans le dictionnaire
               dict_final[l[i]] = l[i + 1]   
   ```
   Solution avec boucle while:
   
   ```Python
       l = ["Schmitt", True, "Irma", False, "Khalif", True, "Yasser", False, "Wang", True]
       dict_final = {}
       i = 0                                 # Variable qui permettra d'itérer et de gérer la boucle while.
       while i < len(l):                     # La boucle s'arrêtera donc au bout de 10 itérations. La valeur maximale de i sera 9.
           if i % 2 == 0:                    
               dict_final[l[i]] = l[i + 1]
           i +=1                             # On incrémente i  
   ```
