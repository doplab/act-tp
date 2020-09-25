# Travaux pratiques semaine 2 solutions


### 1. Typage

Le but de cette partie des travaux pratiques est de comprendre les notions de typage dynamique et statique, ainsi que leur impact sur l’exécution et la gestion des erreurs.

1.1	Quelles sont les principaux types de variable, et comment les déclareriez vous en python et en java ? 
(5 min)

Les principaux types de variables sont les suivants :
Integer (int)
Float
String (str)
Boolean (bool)

En python :
```sh
i = 0
f = 3.14
s = "Hello World"
b = True
```

En java :
```sh
int i = 0
float f = 3.14f
String s = "Hello World"
boolean b = true
```

Il existe d'autres types de variable, comme par exemple les cracartères (char) ou encore les double.

1.2	Parmis ces différents scripts, lesquels pourront être exécutés sans problème et lesquels soulèveront des erreurs ? Expliquez pourquoi 
(5 min)

Java

```sh
var i = 0;
var j = "Hello";
j = i;
```

Ce code ne fonctionnera pas car on essaye de changer le type de la variable j, ce qui est impossible avec un typage statique comme en java. Ici le type de la variable est "déduit" lors de l'exécution du programme

```sh
int i = 0;
String j = "Hello";
j = i;
```

Ce code ne fonctionnera pas car on essaye de changer le type de la variable j, ce qui est impossible avec un typage statique comme en java.

```sh
var i = 0;
i = 3.14 ;
```

Ce code ne fonctionnera pas car on essaye de changer le type de la variable i, ce qui est impossible avec un typage statique comme en java. Ici le type de la variable est "déduit" lors de l'exécution du programme.

```sh
int i = 0;
i = 3.14 ;
```

Ce code ne fonctionnera pas car on essaye de changer le type de la variable i, ce qui est impossible avec un typage statique comme en java. 

Python

```sh
i = 0
j = « Hello »
j = i
```

Ce code fonctionnera sans problème étant donné que le typage des variables en python est dynamique et qu'il est donc possible de changer le type des variables.
```sh
i = 0
i = 3.14
```

Ce code fonctionnera sans problème étant donné que le typage des variables en python est dynamique et qu'il est donc possible de changer le type des variables.^

1.3	Voici deux codes. L’un en java et l’autre en python. Chaque code comporte une fonction nomée raise_error contenant une « Type_Error ». Dans les deux cas, cette fonction ne sera pas appelée lors de l'exécution (la condition est remplie d’office). Pourtant l’un de ces deux codes soulèvera une erreur, et l’autre sera executé sans problème. Quel code soulèvera l’erreur et lequel sera exécuté ? Expliquez pourquoi 
(5min)

Java
```sh
public class Main {

    static void raise_error(){
        int e = 0;
        e = "Bonjour";
    }

    public static void main(String[] args) {

        if (true) {
            System.out.print("OK");
        }
        else {
            raise_error();
        }
    }
}
```

Ce premier code va soulever une Type error, même si la fonction n'est jamais appelée. En java, le typage est dynamique, et de ce fait, toutes les erreurs seront détectées avant exécution du programme.

Python

```sh
def raise_error() :
    print("3" + 5)

if True :
    print("OK")
else :
    raise_error()
```

Ce deuxième code en revanche ne va pas soulever l'erreur. En python le typage est dynamique et de ce fait, l'erreur ne sera détectée qu'au moment ou elle sera executée. Si on change le True en False, la fonction provoquant l'erreur va être appelée, et dans ce cas ci, l'erreur sera mise en évidence.

### 2. Bases en programmation

Le but de cette section est d'écrire vos premières lignes de code. Les notions abordées concerneront les variables, les fonctions, et les interactions avec l'utilisateur (input/output).

2.1 Fonction print()
Initiez une variable `nom` contenant votre nom, et une autre `prénom` contenant votre prénom puis imprimmez : "Bonjour, `prénom` `nom`"
(2 min)

```sh
prénom = "John"
nom = "Doe"
print("Bonjour, " + prénom + " " + nom)
```

2.2 Fonction input() 
Cette fois ci, même exercice mais demandez à l'utilisateur d'entrer son nom et son prénom via la fonction input() au lieu d'initier vous même les variables 
(3min)

```sh
prénom = input("Quel est votre prénom ?")
nom = input("Quel est votre nom ?")
print("Bonjour, " + prénom + " " + nom)
```

2.3 Format d'impression
Demandez 2 variables `nom` et `age` à l'utilisateur, puis imprimmez : "Je m'appelle `prénom` et j'ai `age` ans". Gérez le format de l'impression via l'opérateur +, puis via la fonction format(), et pour finir via l'opérateur %. 
(5min)

```sh
prénom = input("Quel est votre prénom ?")
age = input("Quel est votre age ?")
print("Bonjour, je m'appelle " + prénom + " et j'ai " + age + " ans.")
print("Bonjour, je m'appelle {0} et j'ai {1} ans.".format(prénom,age))
print("Bonjour, je m'appelle %s et j'ai %d ans." % (prénom,age))
```


2.4 Fonction type()
Vous pouvez contrôler le type de vos vraiables via la fonction type(). Déclarez deux variable `nom` (string) et `age` (int), puis imprimmez le type de chacune de ces deux variables
(3min)

```sh
prénom = "John"
age = 23
print(type(prénom))
print(type(age))
```

2.5.1 Conversion des variables
Il est possible de convertir une variable d'un certain type dans un autre type. Il est par exemple possible de changer un Int en Float ou un Float en Int. Déclarez une variable i (Int), puis une variable f (Float). Imprimmez i en le convertissant en Float et f en le convertissant en Int
(3min)

```sh
i = 0
f = 3.14
print(float(i))
print(int(f))
```

2.5.2 Conversion des variables
Attention, ces fonctions ne changent pas le type des variables, elles ne font que les convertir. Quel sera l'output de ces quelques lignes de code ?
(3min)

```sh
i = 3
float(i)
print(type(i))
f = float(i)
print(type(f))
```
<class 'int'>
<class 'float'>

2.6.1 Calculs (multiplication)
Créez 2 variables `facteur_1` (= 11) et `facteur_2` (= 3). Multipliez la première variable par la deuxième et stockez le résultat dans une nouvelle variable `produit`. Vous pouvez imprimmer les différentes variables pour voir leurs valeurs.
Vous pouvez répéter l'exercice avec l'addition et la multiplication.
(3min)

```sh
facteur_1 = 11
facteur_2 = 3
produit = facteur_1*facteur_2
print(facteur_1)
print(facteur_2)
print(produit)
```

2.6.2 Calculs (division)
Créez 2 variables `nb_bonbons` (= 11) et `nb_personnes` (= 3). Divisez la première variable par la deuxième et stockez le résultat dans une nouvelle variable `bonbons_personnes`. Pour finir calculez le nombre de bonbons restants via l'opérateur % (modulo) et stockez le résultat dans `reste`. Vous pouvez imprimmer les différentes variables pour voir leurs valeurs.
Pour la division, essayez tout d'abord avec l'opérateur /, puis avec //. Quelle est la différence ?
(5min)

```sh
nb_bonbons = 11
nb_personnes = 3
bonbons_personnes = nb_bonbons / nb_personnes
reste = nb_bonbons % nb_personnes
print (nb_bonbons)
print(nb_personnes)
print(bonbons_personnes)
print(reste)
```

```sh
nb_bonbons = 11
nb_personnes = 3
bonbons_personnes = nb_bonbons // nb_personnes
reste = nb_bonbons % nb_personnes
print (nb_bonbons)
print(nb_personnes)
print(bonbons_personnes)
print(reste)
```

Le / effectue une division classique, tandis que // effectue une division entière. L'opérateur % n'est ici utile que pour le cas n 2

2.6.3 Calculs (incrémentation / décrémentation)
Gardez vos variables de l'exercice précédent, augmentez la valeur de `nb_bonbons` de 1, et diminuez celle de `nb_personnes` de 1.
(3min)

```sh
nb_bonbons = 11
nb_personnes = 3
nb_bonbons += 1
nb_personnes -= 1
bonbons_personnes = nb_bonbons // nb_personnes
reste = nb_bonbons % nb_personnes
print (nb_bonbons)
print(nb_personnes)
print(bonbons_personnes)
print(reste)
```

2.7.1 Manipulation des Str (indexation)
Créez une variable `python` de type `str` qui vaut "Hard But Cool !!". Créez ensuite une varaible `première` contenant la prmière lettre de `python` en utilisant l'indexation. Créez ensuite une variable `dernière` contenant la dernière lettre de `python`en utilisant l'indexation. Imprimmez les résultats et voyez ce que vous obtenez.
(5min)

```sh
python = "Hard But Cool !!"
première = python[0]
dernière = python[-1]
print(première)
print(dernière)
```

2.7.2 Manipulation des Str (indexation 2)
Gardez votre variable python, et créez une variable `lettre_5` contenant la cinquième lettre de `python` via l'indexation. Créet ensuite une variable `lettre_10_13` contenant les lettres 10,11,12,13 de `python`. Imprimmez les résultats et voyez ce que vous obtenez.
(5min)

```sh
python = "Hard But Cool !!"
lettre_5 = python[4]
lettre_10_13 = python[9:13]
print(lettre_5)
print(lettre_10_13)
```

2.7.3 Manipulation des Str (Fonction len())
Il est possible d'obtenir la longueur d'un str (ou d'une liste ou d'un dictionnaire) via la fonction len(str). Gardez votre variable `python` et créez une nouvelle variable nommée `ln_python` contenant la longeur de `python`, puis une nouvelle variable `moitié` contenant la première moitié de la variable `python` (utilisez la variable que vous venez de créer). Imprimmez le résultat et voyez ce que vous obtenez
(5min)

```sh
python = "Hard But Cool !!"
ln_python = len(python)
moitié = python[:ln_python//2]
print(ln_python)
print(moitié)
```

2.7.4 Manipulation des Str (Fonctions upper() et lower())
Il est possible de passer toutes les lettres d'un str en minuscule ou en majuscule via les fonctions str.lower() et str.upper() respectivement. Comme pour les fonctions int() ou float(), les fonctions upper() et lower() ne modifient pas directement les variables, il faut donc stocker le résultat de ces fonctions dans de nouvelles variables. Reprenez votre variable `python`, puis créez deux nouvelles variables `upper` et `lower` contenant la valeur de `python`en minuscule et en majuscule respectivement. N'oubliez pas d'imprimmez vos nouvelle variables pour voir le résultat.
(5min)

```sh
python = "Hard But Cool !!"
upper = python.upper()
lower = python.lower()
print(upper)
print(lower)
```

2.8.1 Les Fonctions (Fonction basique)
Définissez une fonction nomée `ping` qui lorsqu'elle est appelée imprimme "pong". Appelez la plusieurs fois et voyez le résultat
(3min)

```sh
def ping() :
    print("pong")
    
ping()
ping()
```

2.8.2 Les Fonctions (Fonction multiplication)
Définissez une fonction nomée `multiplicateur`qui prend deux arguments `a` et `b`, les multiplie et retourne le résultat. Stockez le résultat de multiplicateur(2,3) dans une variable `résultat` et imprimmez la.
(5min)

```sh
def multiplicateur(a,b) :
    return(a*b)
    
print(multiplicateur(2,3))
print(multiplicateur(4,5))
```

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

False
True
True
False
False

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

True
False
True
True

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

output 1
output 2
output 4

3.4 Le juste prix
Dans la case suivante, nous vous donnons un nombre aléatoire entre 0 et 30 dans la variable `number` ,
écrivez un programme qui demande à l'utilisateur de deviner le nombre, l'utilisateur a 5 chances pour le
trouver, s'il se trompe, donnez-lui un indice (le nombre qu'il a écrit est-il plus grand ou plus petit que celui
qu'il cherche?). Vous pouvez vous amuser à modifier le nombre de chances ou le nombre de possibilités (par exemple 10 chances pour trouver un nombre entre 0 et 100)

```sh
from random import randint
number = randint(0, 30)
x = int(input("Choississez un nombre: "))
if x == number:
 print("Yeeah!")
elif x < number:
 print("Trop bas!")
else:
 print("Trop haut!")

x = int(input("Choississez un nombre: "))
if x == number:
 print("Yeeah!")
elif x < number:
 print("Trop bas!")
else:
 print("Trop haut!")

x = int(input("Choississez un nombre: "))
if x == number:
 print("Yeeah!")
elif x < number:
 print("Trop bas!")
else:
 print("Trop haut!")

x = int(input("Choississez un nombre: "))
if x == number:
 print("Yeeah!")
elif x < number:
 print("Trop bas!")
else:
 print("Trop haut!")

x = int(input("Choississez un nombre: "))
if x == number:
 print("Yeeah!")
elif x < number:
 print("Trop bas!")
else:
 print("Trop haut!")
```

Le problème avec cette solution c'est que si le joueur trouve la réponse, le jeu va continuer, une façon plus propre de coder ce jeu est d'utiliser une boucle (prochain chapitre)

```sh
from random import randint
number = randint(0, 30)
for i in range(5):
    x = int(input("Choississez un nombre: "))
    if x==number:
        print("Yeah!")
        break
    elif x<number:
        print("Trop petit!")
    else:
        print("Trop grand!")
```

Ici le code est plus concis et permet de s'arrêter lorsque le joueur a trouvé la bonne réponse.

3.5 Pierre, Feuille, Ciseaux
Demandez à l'utilisateur d'entrer soit pierre, soit feuille, soit ciseaux. L'ordinateur lui, choisira son coup au hasard (s'il choisis 1 ce sera pierre, si c'est 2 ce sera feuille et si c'est 3 ce sera ciseaux). Les régles sont les règles classiques, une manche gagnante.

```sh
from random import randint
number = randint(1,3)
if number == 1 :
    ordi = "pierre"
elif number == 2 :
    ordi = "feuille"
else :
    ordi = "ciseaux"
    
player = input("Choississez un signe (pierre, feuille, ciseaux) : ")

print("ordi a choisi " + ordi)

if player != "pierre" and player != "feuille" and player != "ciseaux" :
    print("symbole invalide")
else :
    if ordi == "pierre" :
        if player == "pierre" :
            print("égalité")
        elif player == "feuille" :
            print("gagné")
        else :
            print("perdu")
    elif ordi == "feuille" :
        if player == "pierre" :
            print("perdu")
        elif player == "feuille" :
            print("égalité")
        else :
            print("gagné")
    else :
        if player == "pierre" :
            print("gagné")
        elif player == "feuille" :
            print("perdu")
        else :
            print("égalité")
 ```
 
 Vous pouvez également utiliser une boucle pour augmenter le nombre de manches.