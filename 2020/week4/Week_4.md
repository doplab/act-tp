# Série d'exercice 4: Structure de données, Itération et Récursivité 

### 1. Les structures de données

### 1.1 Les tuples

Pour rappel, les tuples sont des listes d'éléments immuables, ce qui signifie que ces listes ne peuvent pas être modifiées. Les tuples sont utiles pour stocker des données que l'on va réutiliser plus tard.

En Python, pour créer un tuple, il suffit de définir une variable et de lui assigner des valeurs entre parenthèses et séparées entre elles par des virgules:

Exemple:
```Python
mon_tuple = (1,2,3,4)
```

### 1.1.1

Créez un tuple nommé `mon_tuple` contenant les chiffres 1,2,3,4 et 5. Stockez le 4ème élément dans une variable `element_4`, puis affichez la. (5 minutes)

### Conseils

Pour accéder à un élément d'un tuple, ou d'une liste, vous pouvez utiliser l'indexation. Comme pour accéder aux caractères des chaînes de caractères, utilisez [].

### Solutions

```Python
mon_tuple = (1,2,3,4,5)
print(mon_tuple[3])
```

### 1.1.2

Créez un tuple nommé `mon_tuple` contenant les chiffres 1,2,3,4 et 5. Obtenez le nombre d'éléments contenus dans votre tuple et stockez le dans une nouvelle variable nomée `l_mon_tuple`. Pour finir, imprimmez `l_mon_tuple`. (3min)

### Conseils

Pour calculer la taille d'un tuple, ou d'une liste, vous pouvez utiliser la fonction len().

### Solutions

```Python
mon_tuple = (1,2,3,4,5)
l_mon_tuple = len(mon_tuple)
print(l_mon_tuple)
```

### 1.1.3 

Vous pouvez contrôler si un élément est contenu dans un tuple, ou une liste, via l'opérateur `in`. Si l'élément est dans la liste, True vous sera retourné. S'il n'y est pas, True sera retourné. (2min)

Anticipez ce que ce programme imprimera :

```Python
mon_tuple = (1,2,3,4,5,6)

if 6 in mon_tuple :
    print("6 est contenu dans le tuple")
else :
    print("6 n'est pas contenu dans le tuple")
```

#### Solutions

6 est élément de notre tuple, la condition sera donc remplie et c'est "6 est contenu dans le tuple" qui sera imprimmé.

### 1.2 Les listes

La grosse différence entre une liste et un tuple est que l'on peut modifier les éléments d'une liste. Si l'un des éléments de la liste doit être remplacé, il est donc possible de le faire. Il est également possible de retirer ou d'ajouter des éléments.

Pour les créer, il suffit de le définir avec des valeurs entre crochets :

```Python
ma_liste = [1,2,3,4,5]
```

### 1.2.1

Créez une liste nomée `ma_liste`contenant les nombres 1,2,3,4 et 5. Stockez le deuxième élément de la liste dans une variable nomée `element_2`, puis stockez la taille de la liste dans une variable nomée `l_ma_liste`. Imprimez ces deux variables. (5min)

#### Conseils

Comme pour les tuples, vous pouvez utiliser [] pour accéder à un élément, et la fonction len() pour obtenir le nombre d'éléments contenus dans la liste.

#### Solutions

```Python
ma_liste = [1,2,3,4,5]
element_2 = ma_liste[1]
l_ma_liste = len(ma_liste)
print(element_2)
print(l_ma_liste)
```

### 1.2.2

Créez une liste nomée `ma_liste`contenant les nombres 1,2,2,4 et 5. Modifiez le 3ème élément de la liste pour qu'il devienne 2 au lieu de 3. Ajoutez le chiffre 6 à la fin de la liste, et le chiffre 0 au début de cette dernière. (5min)

Utilisez ce morceau de code pour controler que tout a bien été ajouté :

```Python
for c in ma_liste :
    print(c)
```

#### Conseils

Vous pouvez accéder à chaque élément de la liste en utilisant [] et changer sa valeur. Pour ajouter un élément à la fin de la liste, utilisez la fonction append() et pour choisir l'endroit ou vous désirez insérer votre nouvel élément, utilisez la fonction insert().

#### Solutions

```Python
ma_liste = [1,2,2,4,5]
ma_liste[2] = 3
ma_liste.append(6)
ma_liste.append(0,0)
```

### 1.2.3

Créez une liste nomée `ma_liste` contenant les nombres 1,2,3,4 et 5. Vérifiez si le chiffre 6 est dans votre liste. S'il y est, imprimmez "OK", s'il n'y est pas, rajoutez le à votre liste. (5min)

Utilisez ce morceau de code pour controler que tout a bien été ajouté :

```Python
for c in ma_liste :
    print(c)
```

#### Conseils

Comme pour les tuples, vous pouvez utiliser l'opérateur in pour contrôler si un élément est contenu dans votre liste ou non.

#### Solutions

```Python
ma_liste = [1,2,3,4,5]

if 6 in ma_liste :
    print("OK")
else :
    ma_liste.append(6)
```

### 1.3 Les dictionnaires

Les dictionnaires sont des listes associatives, c’est-à-dire des listes qui relient une valeur à une autre. Dans un dictionnaire en papier, les mots sont reliés à leur définition. 

Dans les dictionnaires Python, nous pouvons relier n’importe quelle valeur à n’importe quelle autre valeur (même à ellemême.) Dans un dictionnaire Python, on parle d’une relation clef, valeur. La clef étant le moyen de “retrouver” notre valeur dans notre dictionnaire. Par exemple, dans un dictionnaire en papier, nous pouvons retrouver une définition en cherchant le mot qui lui correspond, alternativement, nous pouvons retrouver le contenu d’une page d’un livre en utilisant le numéro de celle-ci, dans ce cas le numéro est la clef et le texte de la page, la valeur.

Pour créer un dictionnaire, il suffit de lister les couples clé, valeurs entre 2 accolades :

```Python
elon_musk = {
                "prénom": "Elon",
                "nom": "Musk",
                "age": 48,
                "talents": ["programmation", "entrepreunariat", "aéronautique"]
}
```

### 1.3.1

Créez un dictionnaire nommé `fr_eng` contenant les éléments suivants :

"chat": "cat",
"chien": "dog",
"oiseau": "bir",
"poule": "chicken",
"papillon": "butterfly",
"souris": "mouse",
"ours": "bear",
"mouton": "sheep",
"couchon": "pig"

Ce dictionnaire contient des mots en français (les clés) associés à leur traduction en anglais (les valeurs).

Accédez à la traduction du mot "souris", et stockez la dans une variable nomée `souris_traduite`, puis calculez le nombre d'éléments contenus dans le dictionnaire et stockez le dans une variable nomée `l_fr_eng`. Imprimmez les deux variables que vous venez de créer. (5min)

#### Conseils

Comme pour les liste, vous pouvez accéder aux éléments du dictionnaire via les []. Seulement cette fois-ci, au lieu d'y mettre l'indexe, mettez-y la clé associée à l'élément auquel vous voulez accéder.
Comme pour les listes, la fonction len() vous aidera à obtenir le nombre d'éléments dans le dictionnaire.

#### Solutions

```Python
fr_eng = {
                "chat": "cat",
                "chien": "dog",
                "oiseau": "bir",
                "poule": "chicken",
                "papillon": "butterfly",
                "souris": "mouse",
                "ours": "bear",
                "mouton": "sheep",
                "couchon": "pig"
}
souris_traduite = fr_eng["souris"]
l_fr_eng = len(fr_eng)
print(souris_traduite)
print(l_fr_eng)
```

### 1.3.2

Gardez le même dictionnaire qu'auparavant. La traduction du mot "oiseau" est mal orthographiée, modifiez la valeur associée à "oiseau" pour qu'elle devienne "bird".
Ajoutez un nouvel élément au dictionnaire. Associez le mot "horse" au mot "cheval". (5min)

utilisez ce morceau de code pour contrôler vos changements :

```Python
for x in fr_eng :
    print(x + " : " + fr_eng[x])
```

#### Conseils

Comme pour les liste, vous pouvez accéder aux éléments du dictionnaire via les []. Seulement cette fois-ci, au lieu d'y mettre l'indexe, mettez-y la clé associée à l'élément auquel vous voulez accéder.

#### Solutions

```Python
fr_eng = {
                "chat": "cat",
                "chien": "dog",
                "oiseau": "bir",
                "poule": "chicken",
                "papillon": "butterfly",
                "souris": "mouse",
                "ours": "bear",
                "mouton": "sheep",
                "couchon": "pig"
}
fr_eng["oiseau"] = "bird"
fr_eng["cheval"] = "horse"
```

### 1.3.3

Anticipez ce que ce code va imprimmer : (5min)

```Python
elon_musk = {
                "prénom": "Elon",
                "nom": "Musk",
                "age": 48,
                "talents": ["programmation", "entrepreunariat", "aéronautique"]
}

print(elon_musk["talents"][2])
print("aéronautique" in elon_musk["talents"])
```

#### Conseils

Ici l'élément associé à la valeur "talents" du dictionnaire `elon_musk` est une liste.

#### Solutions

aéronautique
True

En effet, via elon_musk["talents"], on accède à la liste ["programmation", "entrepreunariat", "aéronautique"].
Il est donc possible de manipuler cette liste comme une liste classique !


### 2. L'itération

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


#### Note: 
  * La fonction range(n) permet de créer une liste de nombres de 0 à la valeur passée en argument (n). Lorsqu’elle est combinée à une boucle for, on peut itérer sur une liste de nombres de 0 à n-1.
  * Si vous avez fait une erreur dans votre code, il se peut que la boucle while n’arrive jamais à sa condition
et qu’elle ne se termine donc jamais. Ceci peut entraîner un crash de votre programme, voire
même de votre ordinateur. Il faut donc toujours faire attention à la condition de sortie de la boucle while.

#### Attention: Toutes les réponses devront être écrites en python.

### 2.1 Utilisation de la fonction range() dans une boucle for


En utilisant la fonction range() et une boucle for calculez la somme des entier de 0 a 20 et affichez la. (5min)

#### Conseils

* Lorsque range(n) est combinée à une boucle for, on peut itérer sur une liste de nombres de 0 à n-1.

* Déclarer une variable en dehors de la boucle qui contiendra après la boucle la somme.

#### Solutions

```Python
    somme = 0
    for i in range(21):
        somme += i   #A chaque itération on rajoute i à somme. 
    print(somme)
     
 ```
### 2.2 Création d'une liste à partir d'un tuple

Transformer le tuple (1,4,5,8) en une liste à l'aide d'une boucle for. (5min)

#### Conseils

* Déclarer une liste vide é l'extérieur de la boucle.

* La boucle permet d'itérer sur le tuple.

* Rajouter un à un les éléments du tuple dans la liste.

#### Solutions

```Python
    liste_finale = []
    tuple_initial = (1, 4, 5, 8)
    for valeur in tuple_initial:      # A chaque itération valeur est une copie d'un élément du tuple. La boucle se finie au dernier élément du tuple_initial.
        liste_finale.append(valeur)   # On ajoute valeur à la liste crée en dehors de la boucle.
    
     
 ```

### 2.3 Boucle While et input()
   
   A l'aide d'une boucle while, demander à l'utilisateur de rentrer une valeur. Tant que cette valeur ne correspond pas à 10, le programme redemande à l'utilisateur une valeur. (15 min)
   
#### Conseils
   1. Définir à l'extérieur de la boucle le booléen utilisé pour le test dans while.
    
   2. La fonction input() ressort un string ( chaîne de caractères), il faut changer son type. 
  
#### Solutions
  
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
  
### Question 2.4 Boucle While et des étudiants 
  
   Considérons une liste d'étudiants contenant le nom de l'étudiant puis si il était en classe ou non. 
   
   l = ["Schmitt", True, "Irma", False, "Khalif", True, "Yasser", False, "Wang", True]
   
   A partir de cette liste et du type de boucle de votre choix créez un dictionnaire ayant pour clés les noms et comme valeur la présence au cours.
   
#### Conseils
   
   * i % 2: sort le reste de i par la division euclidienne de 2. ( i % 2 == 0 ) Indique si i est pair.
   
   * Boucle for: Utiliser les indices pour accéder aux éléments de la liste et donc ne pas itérer directement sur les éléments de la liste.
   
   * Boucle while: La condition de sortie devrait être en rapport avec la longueur de la liste.
   
#### Solutions
   
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
  * Pour ce problème la boucle for est plus simple à mettre en place et évite le danger de boucle infini. La boucle while est utilisée pour des problèmes plus précis qui ne peuvent pas être résolus par une boucle for. Donc lorsque on peut résoudre un problème avec les deux types, utilisez de préférence la boucle for.
  
### 3. La récursivité

La récursivité est le fait d'appeler une fonction au sein même de cette même fonction. Ce système est souvant utilisé en algorithmique.

### 3.1

Anticipez ce que ces fonctions vont imprimmer : (10min)

3.1.1

```Python
def fonction_p(x) :
    print(x)
    if x == 0 :
        pass
    else :
        fonction_p(x-1)

fonction_p(5)
```


3.1.2

```Python
def fonction_p(x) :
    if x == 0 :
        pass
    else :
        fonction_p(x-1)
        print(x)

fonction_p(5)
```

#### Conseils

La principale différence entre ces 2 codes est l'endroit où est placé le print(). Réfléchissez bien à l'ordre d'exécution de la fonction, écrire le développement sur un papier peut aider.

#### Solutions

3.1.1

5
4
3
2
1
0

3.1.2

0
1
2
3
4
5

### 3.2

Anticipez ce que ce code va imprimmer : (10min)

A quoi sert cette fonction ?

```Python
def fct_a(mot) :

    if len(mot) == 1 :
        if mot[0] == "a" :
            return 1
        else :
            return 0
    else :
        if mot[0] == "a" :
           return 1 + fct_a(mot[1:])
        else :
            return 0 + fct_a(mot[1:])

print(fct_a("blablabla"))
```

#### Conseils

Aidez vous d'un papier et effectuez les étapes une à une afin de bien comprendre comment le code est articulé.

#### Solutions

3

Cette fonction compte le nombre de "a" contenus dans un mot que vous lui passez.

### 3.3

Ecrivez la fonction factoriel() sous forme récursive (5min)

Pour rappel, cette fonction prend un entier et retourne le factoriel de ce dernier.

factoriel(1) = 1, factoriel(2) = 1*2 = 2, factoriel(3) = 1*2*3 = 6, factoriel(4) = 1*2*3*4 = 24,...

#### Conseils

On peut écrire cette fonction comme suit :

f(n) = f(n) * f(n-1) si n > 1
f(n) = 0 si n = 0

#### Solutions

```Python
def factoriel(x) :
        if x == 0:
            return 1
        else :
            return x * factoriel(x-1)
```

### 3.4

Ecrivez deux fonctions permettant de calculer un nombre donné de la suite de Fibonacci.L'une doit utiliser la récursivité, et l'autre l' itérativité. Pour rappel, chaque élément de la suite de Fibonacci est la somme des deux derniers éléments. Le premier élément vaut 0, puis le deuxième et le troisième élément valent tous deux 1. (15min)

Début de la suite : [0,1,1,2,3,5,8,13,...]

#### Conseils

Vous avez déjà vu ces algorithmes quelquepart. Essayez de le faire sans, mais si vous avez des difficultés, l'algorithme est disponible dans le cours (attention il n'est pas en Python).

#### Solutions

Itération :

```Python
def fibonacci_i(n) :
    if n==0 or n==1 :
        return n
    else :
        old_fib = 1
        new_fib = 1
        for i in range(n-2) :
            temp = new_fib
            new_fib = new_fib + old_fib
            old_fib = temp
        return new_fib
```

récursivité :

```Python
def fibonacci_r(n) :
    if n==0 or n==1 :
        return n
    else :
        return fibonacci_r(n-1) + fibonacci_r(n-2)
```
