# Travaux pratiques semaine 2

# Programmation de base

Le but de cette séance est d'aborder des notions de base en programmation. Au terme de cette séance, l'étudiant sera capable de:
- définir une variable, de définir son type et sa valeur.
- Définir une fonction et comprendre son rôle.
- Utiliser des notions d'algèbre booléenne.
- Comprendre la notion d'entrée/sortie.
Les langages qui seront utilisés pour cette séance sont __Java__ et __Python__. Assurez-vous d'avoir bien installé __Pycharm__ et __Netbeans__. Si vous rencontrez des difficultés, n'hésitez pas à vous référer au guide suivant: ** tutoriel d'installation des outils et prise en main de l'environnement de travail **.

### 1. Typage

Le but de cette partie des travaux pratiques est de comprendre les notions de typage dynamique et statique, ainsi que leur impact sur l’exécution et la gestion des erreurs.

1.1	Quelles sont les principaux types de variable, et comment les déclareriez vous en python et en java ? 
(5 min)

1.2	Parmi ces différents scripts, lesquels pourront être exécutés sans problème et lesquels soulèveront des erreurs ? Expliquez pourquoi 
(5 min)

Java

```sh
var i = 0;
var j = "Hello";
j = i;
```

```sh
int i = 0;
string j = "Hello";
j = i;
```

```sh
var i = 0;
i = 3.14 ;
```

```sh
Int i = 0;
I = 3.14 ;
```
Python

```sh
i = 0
j = « Hello »
j = i
```
```sh
i = 0
i = 3.14
```

1.3	Soient les deux programmes suivants, l’un en java et l’autre en python. Chaque programme comporte une fonction nommée raise_error() levant une exception de type « Type_Error ». Dans les deux cas, cette fonction ne sera pas appelée lors de l'exécution (la condition est remplie d’office). Pourtant l’un de ces deux codes soulèvera une erreur, et l’autre sera executé sans problème. Quel code soulèvera l’erreur et lequel sera exécuté ? Expliquez pourquoi 
(5min)

Java
```Java
public class Main {

    static void raise_error(){
        int e = 0;
        e = "Bonjour";
    }

    public static void main(String[] args) {

        if (1==1) {
            System.out.print("OK");
        }
        else {
            raise_error();
        }
    }
}
```

Python

```Python
def raise_error() :
    print("3" + 5)

if 1==1 :
    print("OK")
else :
    raise_error()
```

### 2. Bases en programmation

Le but de cette section est d'écrire vos premières lignes de code. Les notions abordées concerneront les variables, les fonctions, et les interactions avec l'utilisateur (input/output).

2.1 Fonction print()

Créez une variable `nom` contenant votre nom, et une autre `prénom` contenant votre prénom puis affichez : "Bonjour, `prénom` `nom`"
(2 min)


2.2 Fonction input() 
En vous référant à l'exercice précédent, demandez à l'utilisateur d'entrer son nom et son prénom via la fonction input() au lieu d'initialiser vous-même les variables.
(3min)



2.3 Format d'impression

Créer et assignez des valeurs à 2 variables `nom` et `age`, puis affichez: "Je m'appelle `prénom` et j'ai `age` ans". Gérez le format de l'impression via l'opérateur +, puis via la fonction format(), et pour finir via l'opérateur % 
(5min)


2.4 Fonction type()

Vous pouvez contrôler le type de vos variable via la fonction type(). Déclarez deux variable `nom` (string) et `age` (int), puis affichez le type de chacune de ces deux variables.
(3min)


2.5.1 Conversion des variables (`Type casting`)

Il est possible de convertir une variable d'un certain type dans un autre type. Il est par exemple possible de changer un `int` en `float` ou un `float` en `int`. Déclarez une variable i (int), puis une variable f (float). affichez `i` en le convertissant en `float` et `f` en le convertissant en `int`.
(3min)


2.5.2 Conversion des variables (`Type casting`)

Attention, ces fonctions ne changent pas le type des variables, elles ne font que les convertir. Qu'affichera le programme suivant?
(3min)

```Java
i = 3
f = float(i)
print(type(i))
print(type(f))
```

2.6.1 Calculs (multiplication)

Créez 2 variables `facteur_1` (= 11) et `facteur_2` (= 3). Multipliez la première variable par la deuxième et stockez le résultat dans une nouvelle variable `produit`. Vous pouvez afficher les différentes variables pour voir leurs valeurs.
Vous pouvez répéter l'exercice avec l'addition et la multiplication.
(3min)

2.6.2 Calculs (division)

Créez 2 variables `nb_bonbons` (= 11) et `nb_personnes` (= 3). Divisez la première variable par la deuxième et stockez le résultat dans une nouvelle variable `bonbons_personnes`. Pour finir, calculez le nombre de bonbons restants via l'opérateur % (modulo) et stockez le résultat dans `reste`. Vous pouvez afficher les différentes variables pour voir leurs valeurs.
(5min)

2.6.3 Calculs (incrémentation / décrémentation)
Gardez vos variables de l'exercice précédent, augmentez la valeur de `nb_bonbons` de 1, et diminuez celle de `nb_personnes` de 1.
(3min)

2.7.1 Manipulation des chaînes de caractères (indexation)
Créez une variable `python` de type `str` qui vaut "Hard But Cool !!". Créez ensuite une variable `première` contenant la première lettre de `python` en utilisant l'indexation. Créez ensuite une variable `dernière` contenant la dernière lettre de `python`en utilisant l'indexation. Imprimmez les résultats et voyez ce que vous obtenez.
(5min)

2.7.2 Manipulation des Str (indexation 2)
Gardez votre variable python, et créez une variable `lettre_5` contenant la cinquième lettre de `python` via l'indexation. Créet ensuite une variable `lettre_9_13` contenant les lettres 9,10,11,12,13 de `python`. Imprimmez les résultats et voyez ce que vous obtenez.
(5min)

2.7.3 Manipulation des Str (Fonction len())
Il est possible d'obtenir la longueur d'un str (ou d'une liste ou d'un dictionnaire) via la fonction len(str). Gardez votre variable `python` et créez une nouvelle variable nommée `ln_python` contenant la longeur de `python`, puis une nouvelle variable `moitié` contenant la première moitié de la variable `python` (utilisez la variable que vous venez de créer). Imprimmez le résultat et voyez ce que vous obtenez
(5min)

2.7.4 Manipulation des Str (Fonctions upper() et lower())
Il est possible de passer toutes les lettres d'un str en minuscule ou en majuscule via les fonctions lower(str) et upper(str) respectivement. Comme pour les fonctions int() ou float(), les fonctions upper() et lower() ne modifient pas directement les variables, il faut donc stocker le résultat de ces fonctions dans de nouvelles variables. Reprenez votre variable `python`, puis créez deux nouvelles variables `upper` et `lower` contenant la valeur de `python`en minuscule et en majuscule respectivement. N'oubliez pas d'imprimmez vos nouvelle variables pour voir le résultat.
(5min)

2.8.1 Les Fonctions (Fonction basique)
Définissez une fonction nomée `ping` qui lorsqu'elle est appelée imprimme "pong". Appelez la plusieurs fois et voyez le résultat
(3min)

2.8.2 Les Fonctions (Fonction multiplication)
Définissez une fonction nomée `multiplicateur`qui prend deux arguments `a` et `b`, les multiplie et retourne le résultat. Stockez le résultat de multiplicateur(2,3) dans une variable `résultat` et imprimmez la.
(5min)

### 3. Opérateurs et conditions Booléennes

Le principe d'une valeur booléenne est qu'elle ne puisse contenir que 2 valeurs possibles, soit true, soit false. Il est possible de les définir en leur associant une de ces valeurs d'emblée ou de les obtenir en effectuant une comparaison. Pour ce faire, il faut utiliser des opérateurs booléens. Voici les plus utilisés : == (est égal), != (n'est pas égal), < (est strictement plus petit), <= (est plus petit ou égal), > (est strictement plus grand), >= (est plus grand ou égal). Si la condition est satisfaite, on obtiendra true, si elle ne l'est pas, on obtiendra false. L'utilisation de l'opérator not inversera le résultat.

Dans les exerxcices suivants, vous devrez anticiper la valeur que la console va vous donner (résultat du(des) print(s)).

3.1
```sh
a = 3
b = 2
c = 6
d = c >= b
print(a==b)
print(a*b==c)
print(d)
print(a <= b)
print(not d)
```

3.2

```sh
a = 3
b = 2
c = 6
d = c >= b
print(a==b or d)
print(a==b and d)
print(a==b or a==c or False or d)
print(a<c and not (b ==2 and not d))
```

3.3
```sh
a = True
b = False
c = True
if a or (b and not c) :
    print("output 1")
if b!= c :
    print("output 2")
if a or (not b != (c and a)) :
    print("output 3")
if not a or ( b!=c and not b) :
    print("output 3")
```

3.4 Le juste prix
Dans la case suivante, nous vous donnons un nombre aléatoire entre 0 et 30 dans la variable `number` ,
écrivez un programme qui demande à l'utilisateur de deviner le nombre, l'utilisateur a 5 chances pour le
trouver, s'il se trompe, donnez-lui un indice (le nombre qu'il a écrit est-il plus grand ou plus petit que celui
qu'il cherche?). Vous pouvez vous amuser à modifier le nombre de chances ou le nombre de possibilités (par exemple 10 chances pour trouver un nombre entre 0 et 100)

3.5 Pierre, Feuille, Ciseaux
Demandez à l'utilisateur d'entrer soit pierre, soit feuille, soit ciseaux. L'ordinateur lui, choisira son coup au hasard (s'il choisis 1 ce sera pierre, si c'est 2 ce sera feuille et si c'est 3 ce sera ciseaux). Les régles sont les règles classiques, une manche gagnante.
