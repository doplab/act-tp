Algorithmes et Pensée Computationnelle
======================================

# Programmation de base

Le but de cette séance est d'aborder des notions de base en programmation. Au terme de cette séance, l'étudiant sera capable de:
- Définir une variable, de définir son type et sa valeur.
- Définir une fonction et comprendre son rôle.
- Utiliser des notions d'algèbre booléenne.
- Comprendre la notion d'entrée/sortie.

Les langages qui seront utilisés pour cette séance sont __Java__ et __Python__. Assurez-vous d'avoir bien installé __Pycharm__ et __Netbeans__. Si vous rencontrez des difficultés, n'hésitez pas à vous référer au guide suivant: ** tutoriel d'installation des outils et prise en main de l'environnement de travail **.

### 1. Typage

Le but de cette partie des travaux pratiques est de comprendre les notions de typage dynamique et statique, ainsi que leur impact sur l’exécution et la gestion des erreurs.

### 1.1
Quelles sont les principaux types de variable (donnez en 3), et comment les déclareriez vous en __Python__ et en __Java__ ? (5 min)

#### Conseils:

Plusieurs types de variables ont été présentées dans le cours.

#### Solutions :

Les principaux types de variables sont les suivants :
Integer (int)
Float
String (str)
Boolean (bool)

En python :
```Python
i = 0
f = 3.14
s = "Hello World"
b = True
```

En java :
```Java
int i = 0
float f = 3.14f
String s = "Hello World"
boolean b = true
```

Il existe d'autres types de variable, comme par exemple les cracartères (char) ou encore les double.

### 1.2	
Parmi ces différents scripts, lesquels pourront être exécutés sans problème et lesquels soulèveront des erreurs ? S'il y a une erreur, expliquez pourquoi. (5 min)

#### Conseils:

Souvenez vous de la différence principale entre le typage des variables en Java et le typage en Python.


__Java__

```Java
int variable_1 = 0;
int variable_2 = 3;
variable_2 = variable_1;
```

```Java
var variable_1 = 0;
var variable_2 = "Hello";
variable_2 = variable_1;
```

```Java
int variable_1 = 0;
String variable_2 = "Hello";
variable_2 = variable_1;
```

```Java
var variable_1 = 0;
variable_1 = 3.14 ;
```

```Java
var variable_1 = 0;
String variable_2 = "Hello";
String variable_3 = "World"
variable_2 = variable_3;
```

```Java
int variable_1 = 0;
variable_1 = 3.14 ;
```
__Python__

```Python
variable_1 = 0
variable_2 = « Hello »
variable_2 = variable_1
```
```Python
variable_1 = 0
variable_1 = 3.14
```

#### Solutions :

__Java__

1) OK

2) Ce code ne fonctionnera pas car on essaye de changer le type de la variable j, ce qui est impossible avec un typage statique comme en java. Ici le type de la variable est "déduit" lors de l'exécution du programme.

3) Ce code ne fonctionnera pas car on essaye de changer le type de la variable j, ce qui est impossible avec un typage statique comme en java.

4) Ce code ne fonctionnera pas car on essaye de changer le type de la variable j, ce qui est impossible avec un typage statique comme en java. Ici le type de la variable est "déduit" lors de l'exécution du programme.

5) OK

6) Ce code ne fonctionnera pas car on essaye de changer le type de la variable j, ce qui est impossible avec un typage statique comme en java.

__Python__

1) OK

2) OK

### 1.3	
Voici deux programmes, l’un en __Java__ et l’autre en __Python__. Chaque programme comporte une fonction nommée raise_error() levant une exception de type « Type_Error ». Dans les deux cas, cette fonction ne sera pas appelée lors de l'exécution (la condition est remplie d’office). Pourtant l’un de ces deux codes soulèvera une erreur, et l’autre sera executé sans problème. Quel code soulèvera l’erreur et lequel sera exécuté ? Expliquez pourquoi. (5min)

#### Conseils:

Souvenez vous de la différence principale entre le typage des variables en Java et le typage en Python et leur impact sur la compilation / l'interprétation.

__Java__
```Java
public class Main {

    static void raise_error(){
        int variable_1 = 0;
        variable_1 = "Bonjour";
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

__Python__

```Python
def raise_error() :
    print("3" + 5)

if True :
    print("OK")
else :
    raise_error()
```

#### Solutions :

Le premier code va soulever une Type error, même si la fonction n'est jamais appelée. En java, le typage est dynamique, et de ce fait, toutes les erreurs seront détectées avant exécution du programme.

Le deuxième code en revanche ne va pas soulever l'erreur. En python le typage est dynamique et de ce fait, l'erreur ne sera détectée qu'au moment ou elle sera executée. Si on change le True en False, la fonction provoquant l'erreur va être appelée, et dans ce cas ci, l'erreur sera mise en évidence.

### Exercice 2: Représentation de nombres entier ( 30 minutes)

### 2.1 Entiers non signés

  Sur 8 bits écrire (113)<sub>10</sub> en base binaire. (5min)

#### Conseils
  
  * Faire un tableau comme présenté dans le cours page 9 de la semaine 3. Essayer de décomposer en une somme de puissances de 2 le nombre.

#### Solutions

  1. Décomposer le nombre en une somme de puissances de 2.

  113 = 64 + 32 + 16 + 1 = 1 * 2<sup>6</sup> + 1 * 2<sup>5</sup> + 1* 2<sup>4</sup> + 1 * 2<sup>0</sup>

  2.  Inclure les coefficients dans un tableau:

  | 2<sup>7</sup> | 2<sup>6</sup> | 2<sup>5</sup> | 2<sup>4</sup> | 2<sup>3</sup> | 2<sup>2</sup> | 2<sup>1</sup> | 2<sup>0</sup> |
  | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
  | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |

  Donc la représentation en binaire de l'entier non signé (113)<sub>10</sub> est: (01110001)<sub>2</sub>


### 2.2 Entiers signés négatifs 

  En utilisant le résultat de la question précédente, écrire sur 8 bits -113<sub>10</sub> en base binaire. (2min)

### Conseils
  
  * Pour cette représentation, on réserve le 7ème bit pour le signe. 
 
  * Le bit vaut 0 pour un nombre positif et 1 pour un nombre négatif.
  

### Solutions

  | 2<sup>7</sup> | 2<sup>6</sup> | 2<sup>5</sup> | 2<sup>4</sup> | 2<sup>3</sup> | 2<sup>2</sup> | 2<sup>1</sup> | 2<sup>0</sup> |
  | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
  | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |

  Le tableau doit être lu de droite à gauche
  
  Donc l'expression de (-113)<sub>10</sub> en utilisant la représentation d'entiers signés est (11110001)<sub>2</sub>.
  

### 2.3 Complément à 1 

  Ecrire le complément à 1 de -113<sub>10</sub>. 

  Qu'elle est la différence entre cette méthode par rapport à la précédente ? (5min)

#### Conseils 
 
  1. En programmation l'opposé d'une variable est not( la variable). Ici, le même principe s'applique. L'opposé de 0 en binaire est 1. 
  2. Pour étudier la différence, il faut regarder les différenttes manières d'exprimer -0 en binaire ( se référer à la page 10 de la semaine 3).



#### Solutions
  1.

  | 2<sup>7</sup> | 2<sup>6</sup> | 2<sup>5</sup> | 2<sup>4</sup> | 2<sup>3</sup> | 2<sup>2</sup> | 2<sup>1</sup> | 2<sup>0</sup> |
  | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
  | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |
  | not | not | not | not | not | not | not | not |
  | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 |

  2. La portée de cette méthode ne change pas par rapport à celle précédente. Par contre, l'expression de -0 sera différente. 

  **Signed magnitude:** (-0)<sub>10</sub> = (10000000)<sub>2</sub>

  **Complément à 1:** (-0)<sub>10</sub> = (11111111)<sub>2</sub>

  Les deux ont la même portée: portée = [-127<sub>10</sub>,+127<sub>10</sub>] 


### 2.4 Complément à 2 
  
  Quel est le complément à 2 de (-113)<sub>10</sub> et quelle est l'utilitée de cette représentation ? (3min)
  
#### Conseils
  
 1. Voici l'exemple du cours expliqué étape par étape:
 
  | Chiffre et étape | bit 7 | bit 6 | bit 5 | bit 4 | bit 3 | bit 2 | bit 1 | bit 0 |
  | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
  | (87)<sub>10</sub>, étape a | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 1 |    
  | (-87)<sub>10</sub>, étape b | not | not | not | not | not | not | not | not |  
  | (-87)<sub>10</sub>, étape c | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |   
  | (-87)<sub>10</sub>, étape c | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
  | (-87)<sub>10</sub> | (-1) * 2<sup>7</sup> | 0 * 2<sup>6</sup>| 1 * 2<sup>5</sup>| 0 * 2<sup>4</sup> | 1 * 2<sup>3</sup> | 0 * 2<sup>2</sup> | 0 * 2<sup>1</sup> | 1 * 2<sup>0</sup>|
 
   a. Cette étape est la conversion d'un entier positif de base 10 en base 2.
   
   b. Comme pour le complément à 1 on prend l'opposé de chaque bit.
   
   c. On ajoute 1 au bit 0 pour passer à l'étape d'après qui est le complément à 2 de (-87)<sub>10</sub>
   
 2. Il faut regarder si la portée a été modifiée grâce à cette représentation.
  
  
#### Solutions
  
  1. Il faut ajouter 1 au complément à 1 de -113<sub>10</sub>. C'est à dire faire plus 1 à la colonne de 2<sup>0</sup>.
  
  | 2<sup>7</sup> | 2<sup>6</sup> | 2<sup>5</sup> | 2<sup>4</sup> | 2<sup>3</sup> | 2<sup>2</sup> | 2<sup>1</sup> | 2<sup>0</sup> |
  | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
  | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |
  
  2. Il n'y a plus qu'une représentation possible pour (-0)<sub>10</sub>. Il y'a donc un nombre de plus possible par rapport aux dernières représentations. La      nouvelle portée est donc: portée = [-128<sub>10</sub>,+127<sub>10</sub>] 
  
### 2.5 Floating point
  
  Voici la représentation en binaire d'un nombre réel:
  
  | Signe | Exposant | Mantisse |
  | --------- | --------- | --------- | 
  | 0 | 10110101 | 01000001000000000000001 |
  
  Que vaut en base 10 la représentation précédente en utilisant la représentation floating point ? Arrondir les résultats intermédiaires et la valeur finale au 3ème chiffre significatif après la virgule. (10min)
  
#### Conseils
  * Se référer à la diapositive 14 de la semaine 3 pour plus de détails.
  
  * Poser chaque calcul, et ensuite tout fusionner avec la formule. 
  
  * L'exposant et la mantisse sont des entiers positif, donc non signé.
  
  
#### Solutions
  
  *signe* = 0 --> (-1)<sup>sign</sup> = (-1)<sup>0</sup> = 1
  
  *e* = exposant =  1 * 2<sup>7</sup> + 0 * 2<sup>6</sup> + 1 * 2<sup>5</sup> + 1 * 2<sup>4</sup> + 0 * 2<sup>3</sup> + 1 * 2<sup>2</sup> + 0 * 2<sup>1</sup> + 1 * 2<sup>0</sup> = 181
  
  *2<sup>e-127</sup>* = 2<sup>181-127</sup> = 2<sup>54</sup>
  
  mantisse = 01000001000000000000001 = 1 + 0 * 2<sup>-1</sup> + 1 * 2<sup>-2</sup> + 0 * 2<sup>-3</sup> + (...) + 1 * 2<sup>-8</sup> + 1 * 2<sup>-23</sup> = 1.254
  
  Donc Valeur = (+1) * 1.254 * 2<sup>54</sup> = 2.259 * 10<sup>16</sup>
  
### 2.6 Conversion d'un nombre binaire au format complément à 2
 
   Voici un nombre binaire exprimé sur 8 bits au format complément à 2: (10010011)<sub>2</sub>

   Convertir ce nombre en base 10. (5min)

#### Conseils
   
   * Utilisez le même tableau que dans les premières questions.
   
   * On applique le processus inverse au complément à deux. C'est à dire faire les opérations sur le nombre binaire dans le sens inverse que dans les questions 3 et 4.

#### Solutions
   
   Il faut appliquer le processus inverse qu'à la question 3 et 4. Cela permet d'obtenir la valeur positive en binaire du nombre que l'on cherche. Puis il faut convertir cette valeur en base 10 et enfin prendre son inverse.
   
   | Opération | 2<sup>7</sup> | 2<sup>6</sup> | 2<sup>5</sup> | 2<sup>4</sup> | 2<sup>3</sup> | 2<sup>2</sup> | 2<sup>1</sup> | 2<sup>0</sup> |
   | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
   | Aucune| 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 |
   | Soustraction | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
   | Opposition | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1 |
   
   01101101 = 1 + 4 + 8 + 32 + 64 = (109)<sub>10</sub>
   
   Le nombre est donc (-109)<sub>10</sub>

### 3. Bases en programmation

Le but de cette section est d'écrire vos premières lignes de code. Les notions abordées concerneront les variables, les fonctions, et les interactions avec l'utilisateur (input/output). Vous pouvez les écrire en __Java__ ou en __Python__.

### 3.1 Output (__Java__ ou __Python__)

Créez une variable `nom` contenant votre nom, et une autre `prenom` contenant votre prénom puis affichez : "Bonjour, `prenom` `nom`". (2 min)

#### Conseils:

Utilisez la fonction print() in __Python__ / System.out.println() in __Java__ 

#### Solutions :

__Python__

```Python
prenom = "John"
nom = "Doe"
print("Bonjour, " + prenom + " " + nom)
```

__Java__

```Java
String prenom = "John";
String nom = "Doe";
System.out.println("Bonjour, " + prenom + " "+ nom);
```


### 3.2 Input (__Java__ ou __Python__)

En vous référant à l'exercice précédent, demandez à l'utilisateur d'entrer son nom et son prénom via la fonction input() au lieu d'initialiser vous-même les variables. (3min)

#### Conseils:

Utilisez la fonction input() in __Python__ / la classe Scanner() in __Java__ (n'oubliez pas d'ajouter "import java.util.Scanner;") tout au sommet de votre code

#### Solutions :

__Python__

```Python
prenom = input("Quel est votre prénom ?")
nom = input("Quel est votre nom ?")
print("Bonjour, " + prenom + " " + nom)
```

__Java__

```Java
Scanner my_scanner = new Scanner(System.in); 

System.out.println("Entrez votre Prenom : ");
String prenom = my_scanner.nextLine();

System.out.println("Entrez votre Nom : ");
String nom = my_scanner.nextLine();

System.out.println("Bonjour, " + prenom + " "+ nom);
```

### 3.3 Format d'impression (__Python__ uniquement)

Créer et assignez des valeurs à 2 variables `prenom` et `age`, puis affichez: "Je m'appelle `prenom` et j'ai `age` ans". Gérez le format de l'impression via l'opérateur +, puis via la fonction format(). (3min)

#### Conseils:

Ce lien pourrait vous aider avec la fonction format() : https://www.w3schools.com/python/ref_string_format.asp

#### Solutions :

__Python__

```Python
prenom = input("Quel est votre prénom ?")
age = input("Quel est votre age ?")
print("Bonjour, je m'appelle " + prenom + " et j'ai " + age + " ans.")
print("Bonjour, je m'appelle {0} et j'ai {1} ans.".format(prenom,age))
```

### 3.4 Type (__Python__ uniquement)

Déclarez deux variable `nom` (string) et `age` (int), puis affichez le type de chacune de ces deux variables. (3min)

#### Conseils:

Vous pouvez contrôler le type de vos variable via la fonction type()

#### Solutions :

__Python__

```Python
nom = "John"
age = 23
print(type(nom))
print(type(age))
```

### 3.5.1 Conversion des variables (`Type casting`) (__Java__ ou __Python__)

Il est possible de convertir une variable d'un certain type dans un autre type. Il est par exemple possible de changer un `int` en `float` ou un `float` en `int`. Déclarez une variable `nombre_entier` (int), puis une variable `nombre_decimal` (float). Affichez `nombre_entier` en le convertissant en `float` et `nombre_decimal` en le convertissant en `int`. (3min)

#### Conseils:

Utilisez la fonction int(float) et float(int) en __Python__ / Utilisez (int) float et (float) int en __Java__

#### Solutions :

__Python__

```Python
nombre_entier = 0
nombre_decimal = 3.14
print(float(nombre_entier))
print(int(nombre_decimal))
```

__Java__

```Java
int nombre_entier = 0;
float nombre_decimal = 3.14f;
System.out.println((float) nombre_entier);
System.out.println((int) nombre_decimal);
```

### 3.5.2 Conversion des variables (`Type casting`) (__Java__ ou __Python__)

Qu'afficheront les programmes suivants? (3min)

#### Conseils:

Attention, ces fonctions ne changent pas le type des variables, elles ne font que les convertir

__Python__
```Python
nombre_entier = 3
nombre_decimal = float(nombre_entier)
print(nombre_entier)
print(nombre_decimal)
```

__Java__
```Java
float nombre_decimal = 3.14f;
int nombre_entier = (int) nombre_decimal; 
System.out.println(nombre_entier);   
System.out.println(nombre_decimal);      
```

#### Solutions :

__Python__

3
3.0

__Java__

3
3.14

### 3.6.1 Calculs (multiplication) (__Java__ ou __Python__)

Créez 2 variables `facteur_1` (= 11) et `facteur_2` (= 3). Multipliez la première variable par la deuxième et stockez le résultat dans une nouvelle variable `produit`. Vous pouvez afficher les différentes variables pour voir leurs valeurs.
Vous pouvez répéter l'exercice avec l'addition et la multiplication. (3min)

#### Conseils:

L'opérateur de multiplication est le *.

#### Solutions :

__Python__

```Python
facteur_1 = 11
facteur_2 = 3
produit = facteur_1*facteur_2
print(facteur_1)
print(facteur_2)
print(produit)
```

__Java__

```Java
int facteur_1 = 11;
int facteur_2 = 3;
int produit = facteur_1*facteur_2;
System.out.println(facteur_1);
System.out.println(facteur_2);
System.out.println(produit);
```

### 3.6.2 Calculs (division) (__Java__ ou __Python__)

Créez 2 variables `nb_bonbons` (= 11) et `nb_personnes` (= 3). Divisez la première variable par la deuxième et stockez le résultat dans une nouvelle variable `bonbons_personnes`. Pour finir, calculez le nombre de bonbons restants via l'opérateur % (modulo) et stockez le résultat dans `reste`. Vous pouvez afficher les différentes variables pour voir leurs valeurs. (5min)

#### Conseils:

Attention, en __Python__ il existe 2 opérateurs de division, / effectue une division classique, tandis que // effectue une division entière. En __Java__, si vous travaillez uniquement avec des int, / effectuera une division entière tandis que si vous travaillez avec au moins un float, / effectuera une division classique. Vous pouvez aussi formater le type du résultat lorsque vous créez une variable.

#### Solutions :

__Python__

```Python
nb_bonbons = 11
nb_personnes = 3
bonbons_personnes = nb_bonbons // nb_personnes
reste = nb_bonbons % nb_personnes
print (nb_bonbons)
print(nb_personnes)
print(bonbons_personnes)
print(reste)
```

```Python
nb_bonbons = 11
nb_personnes = 3
bonbons_personnes = nb_bonbons / nb_personnes
print (nb_bonbons)
print(nb_personnes)
print(bonbons_personnes)
```


__Java__

```Java
int nb_bonbons = 11;
int nb_personnes = 3;
int bonbons_personnes = nb_bonbons / nb_personnes;
int reste = nb_bonbons % nb_personnes;
System.out.println(nb_bonbons);
System.out.println(nb_personnes);
System.out.println(bonbons_personnes);
System.out.println(reste);
```

```Java
float nb_bonbons = 11;
int nb_personnes = 3;        
float bonbons_personnes = nb_bonbons / nb_personnes;
System.out.println(nb_bonbons);
System.out.println(nb_personnes);
System.out.println(bonbons_personnes);
```
### 3.6.3 Calculs (incrémentation / décrémentation) (__Java__ ou __Python__)

Gardez vos variables de l'exercice précédent, augmentez la valeur de `nb_bonbons` de 1, et diminuez celle de `nb_personnes` de 1. (3min)

#### Conseils:

Vous pouvez utiliser l'opérateur += ou -= en __Python__, et les opérateurs ++ et -- en __Java__.

#### Solutions :

__Python__

```Python
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

__Java__

```Java
int nb_bonbons = 11;
int nb_personnes = 3;
nb_bonbons ++;
nb_personnes --;
int bonbons_personnes = nb_bonbons / nb_personnes;
int reste = nb_bonbons % nb_personnes;
System.out.println(nb_bonbons);
System.out.println(nb_personnes);
System.out.println(bonbons_personnes);
System.out.println(reste);
```

### 3.7.1 Manipulation des chaînes de caractères (indexation) (__Java__ ou __Python__)

Créez une variable `mon_mot` (str) qui vaut "Hard But Cool !!". Créez ensuite une variable `premiere` contenant la première lettre de `mon_mot` en utilisant l'indexation. Créez ensuite une variable `derniere` contenant la dernière lettre de `mon_mot` en utilisant l'indexation. Affichez les résultats et voyez ce que vous obtenez. (5min)

#### Conseils:

Pour __Python__, utilisez [], et pour __Java__, utilisez la fonction substring() ainsi que la fontion length().

#### Solutions :

__Python__

```Python
mon_mot = "Hard But Cool !!"
premiere = mon_mot[0]
derniere = mon_mot[-1]
print(premiere)
print(derniere)
```

__Java__

```Java
String mon_mot = "Hard But Cool !!";
String premiere = mon_mot.substring(0,1);
String derniere = mon_mot.substring(mon_mot.length()-1);
System.out.println(premiere);
System.out.println(derniere);
```

### 3.7.2 Manipulation des chaînes de caractères (indexation 2) (__Java__ ou __Python__)

Gardez votre variable, `mon_mot` et créez une variable `lettre_5` contenant la cinquième lettre de `mon_mot` via l'indexation. Créez ensuite une variable `lettre_9_13` contenant les lettres 9,10,11,12,13 de `mon_mot`. Afficher les résultats et voyez ce que vous obtenez. (5min)

#### Conseils:

Attention, ici les espaces comptent comme des caractères !

Pour __Python__, utilisez [:], et pour __Java__, utilisez la fonction substring()

#### Solutions :

__Python__

```Python
mon_mot = "Hard But Cool !!"
lettre_5 = mon_mot[4]
lettre_10_13 = mon_mot[9:13]
print(lettre_5)
print(lettre_10_13)
```

__Java__

```Java
String mon_mot = "Hard But Cool !!";
String lettre_5 = mon_mot.substring(4,5);
String lettre_10_13 = mon_mot.substring(9,13);
System.out.println(lettre_5);
System.out.println(lettre_10_13);
```


### 3.7.3 Manipulation des chaînes de caractères (__Java__ ou __Python__)

Il est possible d'obtenir la longueur d'une chaîne de caractère (ou d'une liste ou d'un dictionnaire) via la fonction `len()`. Gardez votre variable `mon_mot` et créez une nouvelle variable nommée `ln_mon_mot` contenant le nombre de caractère de la variable `mon_mot`, puis une nouvelle variable `moitié` contenant la première moitié de la variable `mon_mot` (utilisez la variable que vous venez de créer). Affichez le résultat et voyez ce que vous obtenez. (5min)

#### Conseils:

La fonction présentée dans l'énnoncé de la question n' est valable que pour __python__. L'équivalent pour __Java__ est la fonction length()

#### Solutions :

__Python__

```Python
mon_mot = "Hard But Cool !!"
ln_mon_mot = len(mon_mot)
moitie_mon_mot = mon_mot[:ln_mon_mot//2]
print(ln_mon_mot)
print(moitie_mon_mot)
```

__Java__

```Java
String mon_mot = "Hard But Cool !!";
int ln_mon_mot = mon_mot.length();
String moitie = mon_mot.substring(0,ln_mon_mot/2);
System.out.println(ln_mon_mot);
System.out.println(moitie);
```



### 3.8.1 Les Fonctions (Fonctions basiques) (__Java__ ou __Python__)
Définissez une fonction nommée `ping()` qui, lorsqu'elle est appelée, affiche "pong". Appelez la plusieurs fois et voyez le résultat. (3min)

#### Conseils:
Vous pourriez utiliser une boucle `for` pour effectuer plusieurs appels à la fonction `ping()`.

#### Solutions :

__Python__

```Python
def ping() :
    print("pong")
    
ping()
ping()
```

__Java__

```Java
public class Main {

    static void Ping(){
        System.out.println("Pong");
    }

    public static void main(String[] args) {
        Ping();
        Ping();
    }
}
```

### 3.8.2 Les Fonctions (Fonction multiplication) (__Java__ ou __Python__)

Définissez une fonction nommée `multiplicateur()` qui prend deux arguments `multiple_1` et `multiple_2`, les multiplie et retourne le résultat. Stockez le résultat de `multiplicateur(2,3)` dans une variable `resultat` et affichez la. (5min)

#### Solutions :

__Python__

```Python
def multiplicateur(a,b) :
    return(a*b)
    
print(multiplicateur(2,3))
print(multiplicateur(4,5))
```

__Java__

```Java
public class Main {

    static int Multiplicateur(int a, int b){
        return a*b;
    }

    public static void main(String[] args) {
        System.out.println(Multiplicateur(2,3));
    }
}
```

### 4. Opérateurs et conditions Booléennes (__Python__ uniquement)

Le principe d'une valeur booléenne est qu'elle ne puisse contenir que 2 valeurs possibles, soit `True`, soit `False`. Il est possible de les définir en leur associant une de ces valeurs d'emblée ou de les obtenir en effectuant une comparaison. Pour ce faire, il faut utiliser des opérateurs booléens. Voici les plus utilisés : == (est égal), != (n'est pas égal), < (est strictement plus petit), <= (est plus petit ou égal), > (est strictement plus grand), >= (est plus grand ou égal). Si la condition est satisfaite, on obtiendra `True`, si elle ne l'est pas, on obtiendra `False`. L'utilisation de l'opérateur `not` inversera le résultat.

Dans les exercices suivants, vous devrez anticiper la valeur que la console va vous donner (résultat du(des) print(s)).

#### Conseils:

Utilisez les tables de vérité des `and` et des `or`

### 4.1 (5min)
```Python
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

#### Solutions :

False
True
True
False
False

### 4.2 (5min)

```Python
a = 3
b = 2
c = 6
d = c >= b
print(a==b or d)
print(a==b and d)
print(a==b or a==c or False or d)
print(a<c and not (b ==2 and not d))
```

#### Solutions :

True
False
True
True

### 4.3 (5min)
```Python
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

#### Solutions :

output 1
output 2
output 4

### 5. Conditions ( 10 minutes)

  Le but de cet exercice est d'entrainer la lecture de code, la compréhension des opérateurs booléens ainsi que le "case switching" à travers le branchement conditionnel.
  
### 5.1 Branchement conditionnel en java (5 minutes)
  
   Qu'affiche le code suivant ? (5min)
   
   Rappel: Le code suivant est en Java
   
  ```Java
    int numero_mois = 7
    
    switch(numero_mois) {
      
        case 1:
                  System.out.println("Janvier");
                  break;
        case 2:
                  System.out.println("Février");
                  break;
        case 3:
                  System.out.println("Mars");
                  break;
        case 4:
                  System.out.println("Avril");
                  break;
        case 5:
                  System.out.println("Mai");
                  break;
        case 6:
                  System.out.println("Juin");
                  break;
        case 7:
                  System.out.println("Juillet");
                  numero_mois = 9 ;
        case 8:
                  System.out.println("Août");
        case 9:
                  if (numero_mois == 8){
                    System.out.println("Septembre");
                    break;
                    }
                   else{
                     System.out.println("Décembre");
                     numero_mois = 13;
                     break;
                     }
        case 10:
                  System.out.println("Octobre")
                  break;
        case 11:
                  System.out.println("Novembre")
                  break;
        case 12:
                  System.out.println("Décembre")
                  break;
        default:
                  System.out.println("Ce n'est pas un mois. ");
   }
```
#### Conseils
  
  1. Break indique que l'on sort de l'accolade. Les cas suivants ne seront pas traités. 
  
  2. L'absence de break indique que l'on va rentrer dans tous les cas suivants.
  
  3. Lorsque l'on pose "case n" où n est un nombre cela est équivalent au test n == numero_mois. Ce test est aussi valable si on cherche a comparer des chaînes de caractères ( par exemple si numero_mois = " Juin", à ce moment là n sera aussi une chaîne de caractères).
  
#### Solutions
  
  Le code va donc afficher:
  
  Juillet
  Août
  Décembre 
  
#### Explications 
  
  1. Comme la case 7 ne contient pas de break et modifie numero_mois, la lecture du code va continuer.
  
  2. On rentre dans le case 9, qui contient un break. Le numero_mois sera aussi modifié mais cela ne sera pas important car on sort de l'accolade et les cas succédants ne seront pas traités.
  
### 5.2 Conditionnal branching in python
  
  Qu'affiche le code suivant ? (5min)
  
  Rappel: Ce code est en python. 
  
  ```Python
  
      name = "Garbinato"
      assistant = "Diallo"
      lesson = "ACT"
      if ((name == "Diallo") or not(name == "Garbinato")) and (lesson = "ACT"):
          print("Alpha et Garbinato")
      elif ((name == "Michelet") and (lesson = "ACT")) or ( name == lesson):
          print("Gaëtan")
      elif (name == " Yasser Haddad" or assistant = "Diallo") and (lesson == "ACT and name == "Olivier"):
          print("Yann")
      elif ((name == "Garbinato" or lesson == "INF") and assistant == " Diallo") or (lesson == "ACT" and name = "Diallo"):
          print("Teacher" + " Algorithmique et pensée computationelle.")
      else:
          print("Benoît")
      
     
 ```
#### Conseils
  
  1. Il faut vérifier la condition de chaque cas de manière linéaire.
  
  2. Une fois une condition vérifiée, toutes celles d'après ne sont pas traitées.
  
#### Solutions

  Le code affiche:
  
  Teacher Algorithmique et pensée computationelle.
  
  
#### Explications

  Ci-dessous, le résultat des propositions booléennes des if et elif:
  
  1. (False or False) and True = False 
  
  2. (False and True) or False = False 
  
  3. (False or True) and ( True and False) = True and False = False
  
  4. ((True or True) and True) or ( True and True) = True


### 6. Exercices pour aller plus loin, facultatifs mais recommandés (Solutions en __Python__ uniquement)

Ces deux exercices sont des créations de petits jeux bien connus, et relativement rapides à implémenter.

### 6.1 Le juste prix (20min)
Dans la case suivante, nous vous donnons un nombre aléatoire entre 0 et 30 dans la variable `number` ,
écrivez un programme qui demande à l'utilisateur de deviner le nombre, l'utilisateur a 5 chances pour le
trouver, s'il se trompe, donnez-lui un indice (le nombre qu'il a écrit est-il plus grand ou plus petit que celui
qu'il cherche?). Vous pouvez vous amuser à modifier le nombre de chances ou le nombre de possibilités (par exemple 10 chances pour trouver un nombre entre 0 et 100).

#### Conseils:

Vous pouvez ajouter une boucle for avec la fonction range(5) pour simplifier le code !

#### Solutions :

```Python
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

```Python
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

### 6.2 Pierre, Feuille, Ciseaux (20min)
Demandez à l'utilisateur d'entrer soit pierre, soit feuille, soit ciseaux. L'ordinateur lui, choisira son coup au hasard (s'il choisi 1 ce sera pierre, si c'est 2 ce sera feuille et si c'est 3 ce sera ciseaux). Les règles sont les règles classiques, une manche gagnante.

#### Solutions :

```Python
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
