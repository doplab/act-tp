# Banque des questions

### Exercice 1

Dans cet exercice, nous aimerions que le processeur calcule et enregistre le produit de 3 fois $10_{10}$ ($00001010_2$) dans le registre 11. Le program counter (PC) commence à **00000100** et les registres sont initialisés comme suit :

| Registre | Valeur |
| :--- | :--- |
| 00 | 00001010 |
| 01 | 00000000 |
| 10 | 00000000 |
| 11 | 00000000 |

Les opérations disponibles sont :

| Numéro | Instruction |
| :---: | :---: |
| 00 | MOV |
| 01 | XOR |
| 10 | ADD |
| 11 | SUB |

**a.** Complétez le tableau ci-dessous avec les instructions en binaire nécessaires pour effectuer cette tâche.

| Adresse | Valeur |
| :--- | :--- |
| 00000100 | |
| 00000101 | |

**b.** Donnez le contenu des registres après l'exécution de la première instruction et après l'exécution de la deuxième instruction.

| Registre | Après 1ère instruction | Après 2ème instruction |
| :---: | :--- | :--- |
| 00 | | |
| 01 | | |
| 10 | | |
| 11 | | |

-----

### Exercice 2

Quel est le résultat de la soustraction hexadécimale suivante : $694F - 5A3C$ ?

-----

### Exercice 3

Selon le modèle de Von Neumann, partant d'un program counter valant **101010** et d'une mémoire contenant les instructions suivantes :

| Adresse | Instruction |
| :---: | :---: |
| 101001 | 01000111 |
| 101010 | 01111000 |
| 101011 | 10001101 |
| 101100 | 10010110 |

À quelle adresse le résultat de la prochaine opération va-t-il être stocké ?

(A) 00
(B) 01
(C) 10
(D) 11

-----

### Exercice 4

Quel est le résultat de l'opération suivante : $395_{16} + 1011101_{2}$ ?

(A) $1010_{10}$
(B) $3E2_{16}$
(C) $0011\ 1110\ 0010_2$
(D) $1010_2$

-----

### Exercice 5

Quelle est la valeur en base 10 de l’opération suivante : $128_9 - 245_6$ ?

(A) 9
(B) 6
(C) 0
(D) 3

-----

### Exercice 6

Convertir le nombre $127_{10}$ en base 8.

(A) 87
(B) 177
(C) 71
(D) 180

-----

### Exercice 7

Quel est le résultat de l'opération suivante $67_8 + 110111_2$ en base 10 ?

(A) 110
(B) 78
(C) 122
(D) 106

-----

### Exercice 8

En suivant le modèle de von Neumann, l'instruction register (IR) a une valeur de **11000111**, les registres contiennent les valeurs suivantes :

| Registre | Valeur |
| :---: | :---: |
| 00 | 00000000 |
| 01 | 00000101 |
| 10 | 00000110 |
| 11 | 00000010 |

Table des opérations :
| Numéro | Valeur |
| :---: | :---: |
| 00 | MOV |
| 01 | XOR |
| 10 | ADD |
| 11 | SUB |

Quelle est la valeur du résultat de l'opération ?

(A) $111_2$
(B) $1011_2$
(C) $011_2$
(D) $0001_2$

-----

### Exercice 9

*(Note : Cet exercice semble être une duplication du texte de la question précédente sans contexte, mais voici les options fournies)*
Quelle est la valeur du résultat de l'opération ?

(A) $111_2$
(B) $1011_2$
(C) $011_2$
(D) $0001_2$

-----

### Exercice 10

Que représentent les deux premiers bits de l'instruction register ? (exemple : **11**001001) ?

(A) L'adresse du registre dans lequel il faudra mettre le résultat
(B) L'identificateur de l'opération à exécuter
(C) L'adresse du registre dans lequel est contenue la valeur sur laquelle faire l'opération
(D) Ils n'ont aucune signification

-----

### Exercice 11

Quel est le résultat de la soustraction $11011001_2 - 00110110_2$ en base 10 ?

-----

### Exercice 12

Quel est le résultat de l'opération suivante : $1011010_2 - 1000111_2$ ?

(A) $0001111_2$
(B) $0010011_2$
(C) $0100011_2$
(D) $0010101_2$

-----

### Exercice 13

Quel est le résultat en base 10 de l'opération suivante : $47_{10} + DEF_{16}$ ?

(A) 3614
(B) 3478
(C) 3589
(D) 3641

-----

### Exercice 14

Quel est l'avantage principal d'un langage compilé ?

(A) Plus facile à corriger
(B) Exécution plus rapide
(C) Plus simple à écrire que les autres langages
(D) Indépendant du système d’exploitation

-----

### Exercice 15

Quelle est la différence entre un compilateur et un interpréteur ?

(A) Le compilateur traduit le code au moment de l’exécution, l’interpréteur avant l’exécution
(B) Le compilateur traduit le code avant l’exécution, l’interpréteur au moment de l’exécution
(C) Les deux font exactement la même chose
(D) Le compilateur n’est utilisé que pour les systèmes Unix

-----

### Exercice 16

Voici la visualisation de vos dossiers (exemple : Dans le dossier Cours il y a un dossier Cours\_1) :

```text
/User
├── /Cours
│   └── /Cours_1
│       └── Slides_1.pdf
├── /TPs
│   ├── /Solutions
│   ├── tp1.py
│   └── tp1.java
├── /Documents
└── /Photos
```

Vous ouvrez un terminal et vous êtes dans le dossier **TPs**, qu'est-ce qui va être affiché dans le terminal si vous tapez `ls` (on écrit tout à la même ligne par souci de concision) :

(A) Solutions tp1.py tp1.java
(B) TPs Solutions tp1.py tp1.java
(C) Cours Cours\_1 Slides\_1 TPs Solutions tp1.py tp1.py Photos Documents
(D) tp1.py tp1.java

-----

### Exercice 17

Vous êtes toujours dans le dossier **TPs** et vous voulez aller dans le dossier **Solutions**, quelle commande tapez-vous dans le terminal ?

(A) `rm Solutions`
(B) `mv Solutions`
(C) `cd Solutions`
(D) `mkdir Solutions`

-----

### Exercice 18

Vous vous trouvez dans un dossier qui contient deux sous-dossiers : **python** et **java**.

  * Le dossier **python** contient un unique fichier nommé `hello.py`.
  * Le dossier **java** contient un unique fichier nommé `hi.java`.

**(a)** Quelle(s) commande(s) devez-vous taper dans le terminal, ouvert depuis le dossier **parent** de python, pour exécuter le programme *hello.py* ?

**(b)** Après avoir exécuté les commandes de la question (a), quelles commandes faut-il saisir pour compiler puis exécuter le programme *hi.java* situé dans le dossier *java* ?

**(c)** Après avoir exécuté le programme *hi.java*, si vous vous placez dans le dossier *java* et que vous tapez la commande **ls**, quelle sera la sortie affichée dans le terminal ?

-----

### Exercice 19

La commande `pwd` sous Linux/MacOS permet de :

(A) Afficher le chemin absolu du répertoire courant
(B) Supprimer le répertoire courant
(C) Créer un nouveau fichier
(D) Afficher la liste des fichiers dans le répertoire courant

-----

### Exercice 20

Parmi ces commandes Linux/MacOS, laquelle permet de créer un nouveau répertoire ?

(A) `ls`
(B) `cd`
(C) `mkdir`
(D) `pwd`

-----

### Exercice 21

Voici la ligne de commande d'un terminal sur une machine MacOS/Linux (à gauche) et Windows (à droite).
*[Image: bashq21.pdf]*

Quelle commande a été passée (\#LINE REMOVED) ?

(A) `dir`
(B) `cd Users`
(C) `cd ..`
(D) `ls`

-----

### Exercice 22

Laquelle des affirmations suivantes est fausse ?

(A) Un langage compilé est traduit ligne par ligne au moment de l'exécution
(B) En Java, l'étape de compilation et d'interprétation sont séparées
(C) Un langage interprété est plus lent à exécuter
(D) Les langages python et java nécessitent les deux une traduction en bytecode
(E) Toutes les affirmations sont correctes

-----

### Exercice 23

En Java, que signifie le mot-clé `final` appliqué à une variable ?

(A) La variable ne peut pas être utilisée dans une boucle
(B) La variable est constante et ne peut pas changer de valeur
(C) La variable est automatiquement initialisée à zéro
(D) La variable est globale

-----

### Exercice 24

Si on exécute le code suivant :

```python
x = 7
if x % 2 == 0:
   print("pair")
else:
   print("impair")
```

Que sera affiché ?

(A) impair
(B) pair
(C) 7
(D) Aucun affichage

-----

### Exercice 25

Qu'affiche le code suivant écrit en Java ?

```java
int numero_jour = 5;
switch (numero_jour) {
    case 1:
        System.out.println("Lundi");
        break;
    case 2:
        System.out.println("Mardi");
        break;
    case 3:
         System.out.println("Mercredi");
         break;
     case 4:
          System.out.println("Jeudi");
          break;
     case 5:
          System.out.println("Vendredi");
     case 6:
          System.out.println("Samedi");
          break;
     case 7:
          System.out.println("Dimanche");
          break;
     default:
           System.out.println("Ce n'est pas un jour valide !");
}
```

(A) Vendredi
(B) Vendredi Samedi Dimanche
(C) Ce n'est pas un jour valide
(D) Vendredi Samedi

-----

### Exercice 26

Qu'affiche le code suivant écrit en Python ?

```python
a = False
b = True
c = False

if (a or b) and (a or not c):
    print("output 1")
elif (a or not b) and (a or c):
    print("output 2")
if (a or not b) and (a or not c):
    print("output 3")
else:
    print("output 4")
```

(A) output 1
(B) output 1 output 4
(C) output 4
(D) output 1 output 3

-----

### Exercice 27

Ecrivez le complément à 2 de $21_{10}$ sur 8 bits :

(A) 1110 1011
(B) 1110 1010
(C) 0001 0101
(D) 0001 0100

-----

### Exercice 28

Laquelle des affirmations suivantes est correcte concernant l'expression :

$$((\neg p \wedge q) \wedge (\neg p \vee \neg q)) \vee ((p \wedge q) \wedge \neg q)$$

(A) Si p est faux et q est vrai, l'expression est fausse
(B) Si p est vrai et q est faux, l'expression est fausse
(C) Si p est faux et q est faux, l'expression est vraie
(D) Toutes les affirmations sont correctes

-----

### Exercice 29

On attribue à une variable `variable1` la valeur 2. On attribue à une variable `variable2` la valeur "hello". On essaie ensuite d'attribuer à `variable2` la valeur de `variable1` (en écrivant `variable2 = variable1`). Laquelle des affirmations suivantes est correcte ?

(A) En Java, le code va afficher une erreur
(B) En Java, le code va afficher une erreur, à moins que les variables aient été les deux déclarées de type var
(C) En Python, le code va afficher une erreur
(D) En Python, le code va convertir l'entier deux en la chaîne de caractère "2" pour l'attribuer à variable2

-----

### Exercice 30

Qu'affiche le programme Java suivant ?

```java
public class Test {
  public static void main(String[] args) {
    int a = 5;
    int b = 3;
    boolean c = (a > b) && (b > 10);
    System.out.println(c);
  }
}
```

(A) True
(B) False
(C) Le programme provoque une erreur de compilation
(D) c

-----

### Exercice 31

Quelle est la représentation du complément à 2 (two complement) de -143 sur 8 bits ?

(A) 10010001
(B) 01110001
(C) 01100001
(D) Aucune des réponses n'est correcte

-----

### Exercice 32

Qu'affiche le programme Java suivant ?

```java
public class Test {
  public static void main(String[] args) {
    int a = 5;
    int b = 3;
    boolean c = (a > b) && ((b < 10) || (a < b)) || (a == b);
    System.out.println(c);
  }
}
```

(A) True
(B) False
(C) Le programme provoque une erreur de compilation
(D) c

-----

### Exercice 33

Dans la table de vérité suivante, par quelle expression faut-il remplacer \#LINE REMOVED pour obtenir la troisième colonne ?

| p | q | \#LINE REMOVED |
| :---: | :---: | :---: |
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

(A) $((\neg p \vee q) \wedge (p \vee \neg q))$
(B) $(\neg ((p \wedge q) \vee (\neg p \wedge \neg q)))$
(C) $((p \vee q) \wedge \neg (p \wedge q))$
(D) $\neg (p \wedge q)$
(E) Aucune des réponses n'est correcte

-----

### Exercice 34

Soit la fonction $f(p,q) = (\neg p) \vee (\neg q)$, par quelle expression faut-il remplacer \#LINE REMOVED dans le code Java suivant pour que la méthode `computeF(boolean p, boolean q)` soit équivalente à la fonction $f$ ?

```java
public static boolean computeF(boolean p, boolean q){
    return #LINE REMOVED;
}
```

(A) `p && (q || !q)`
(B) `p || !q`
(C) `!(p && q)`
(D) `not p or not q`
(E) Aucune des réponses n'est correcte

-----

### Exercice 35

Quelle expression est équivalente à l'expression $\neg( \neg (A \wedge A) \wedge \neg(B \wedge B))$ :

(A) $A \lor B$
(B) $A \land B$
(C) $(\lnot A \lor \lnot B)$
(D) $\lnot(A \lor B)$
(E) Aucune des réponses n'est correcte

-----

### Exercice 36

En Python, quel opérateur réalise une division entière ?

(A) `/`
(B) `%`
(C) `//`
(D) `div()`

-----

### Exercice 37

En Python, quelle exception sera levée pour une division par zéro ?

(A) `ValueError`
(B) `TypeError`
(C) `ZeroDivisionError`
(D) `ArithmeticError`

-----

### Exercice 38

Parmi les éléments suivants, lesquels ne sont pas contenus dans une *stack frame* :

a) Une adresse de retour
b) Les variables
c) Une valeur de retour
d) Les fonctions appelées
e) Tous ces éléments sont contenus dans une *stack frame*

-----

### Exercice 39

Qu'affiche le code suivant ?

```java
static void z(int a){
    System.out.print("z");
    if (a > 1){
        y(a);
    }
}

static void y(int a){
    System.out.print("y");
    if (a == 0){
        System.out.print(0);
    }
    else{
        a = 0;
        x(a);
    }
}

static void x(int a){
    System.out.print("x");
    if (a == 0) {
        y(a);
    }
    else{
        z(a);
    }
}

static void main() {
    x(2);
}
```

a) xz
b) xzyxy0
c) xzy0
d) Une erreur

-----

### Exercice 40

Qu'affiche le programme suivant supposant que l'utilisateur saisit l'entrée suivante ?

Entrez votre username : "Algo1"
Entrez votre password : "2025-2026"

```python
user = "Algo"
password = "2025-2026"
try:
    user_1 = input("Entrez votre username : ")
    password_1 = input("Entrez votre mot de passe :")
    if not (user == user_1) :
        raise NameError
    else:
        if (password == password_1) :
            raise PermissionError
        else :
            print("Vous êtes connecté !")
except NameError as error :
    print("L'username n'est pas correct")
except PermissionError as error:
    print("Le mot de passe ne correspond pas à l'username")
```

a) L'username n'est pas correct Le mot de passe ne correspond pas à l'username
b) L'username n'est pas correct
c) Vous êtes connecté
d) Le mot de passe ne correspond pas à l'username

-----

### Exercice 41

Maintenant qu'affiche le programme suivant supposant que l'utilisateur saisit l'entrée suivante ?

Entrez votre username : "Algo"
Entrez votre password : "2025-2027"

a) L'username n'est pas correct Le mot de passe ne correspond pas à l'username
b) L'username n'est pas correct
c) Vous êtes connecté
d) Le mot de passe ne correspond pas à l'username

-----

### Exercice 42

Qu'affiche le programme suivant ?

```python
prix_de_groupe = 40
nb_personne = 5
prix_par_personne = prix_de_groupe / nb_personne
print(f"Le prix est de : {prix_par_personne} chf pour un groupe de {nb_personne}")
nb_personne += 1
prix_par_personne = prix_de_groupe//nb_personne
print(f"Le prix est de : {prix_par_personne} chf pour un groupe de {nb_personne}")
```

a)
Le prix est de : 8.0 chf pour un groupe de 5
Le prix est de : 6 chf pour un groupe de 6

b)
Le prix est de : 8 chf pour un groupe de 5
Le prix est de : 6 chf pour un groupe de 6

c)
Le prix est de : 8 chf pour un groupe de 5
Le prix est de : 6.66666666667 chf pour un groupe de 6

d)
Le prix est de : 8.0 chf pour un groupe de 5
Le prix est de : 6.66666666667 chf pour un groupe de 6

-----

### Exercice 43

Voici un programme composé de 4 fonctions additions :

```java
public class Question3 {
    public static void main(String args[]) {
        System.out.println("Question3");
    }
    public static ??? addition_1 (int a, int b){
        return a + b;
    }
    public static ??? addition_2 (int a, double b){
        return a + b;
    }
    public static ??? addition_3(String a, String b){
        return a + b;
    }
    public static ??? addition_4 (double a, double b){
        System.out.println(a + b);
    }
}
```

Indiquez pour chaque fonction addition par quel type on doit remplacer les `???` pour que le programme fonctionne :

addition\_1 :
addition\_2 :
addition\_3 :
addition\_4 :

-----

### Exercice 44

Qu'affiche le code suivant (Python) ?

```python
try:
   x = int("10")
   try:
       y = int("texte")
   except ValueError:
       print("Erreur interne détectée")
   finally:
       print("Bloc interne terminé")
except Exception:
   print("Erreur externe")
finally:
    print("Bloc externe terminé")
```

a. Erreur externe / Bloc externe terminé
b. Erreur interne détectée / Bloc interne terminé / Bloc externe terminé
c. Bloc interne terminé / Erreur externe
d. Erreur interne détectée / Erreur externe

-----

### Exercice 45

Laquelle des affirmations suivantes est incorrecte ?

a. Une fonction en Java doit spécifier un type de retour (même void si elle ne retourne rien).
b. Le mot-clé public est obligatoire devant toute fonction.
c. Les parenthèses sont obligatoires même si la fonction ne prend aucun paramètre.
d. En Java, une fonction (méthode) doit toujours être déclarée à l’intérieur d’une classe.

-----

### Exercice 46

Qu'affiche le programme suivant ?

```java
int i = 1;
while (i % 5 != 0) {
    System.out.print(i);
    i++;
    if (i == 5) {
        i++;
    }
}
System.out.println(i);
```

a) 1 2 3 4 5 6 7 8 9 10
b) 1 2 3 4 6 7 8 9 10
c) 1 2 3 4 5 6 7 8 9
d) Le programme continue en boucle

-----

### Exercice 47

Si maintenant on rajoute une nouvelle partie au programme, le programme est maintenant comme suit :

```java
int i = 1;
while (i % 5 != 0) {
    System.out.print(i);
    i++;
    if (i == 5) {
        i++;
    }
}
System.out.println(i);

// Nouvelle partie du programme
int j = 0;
while (j % 3 == 0) {
    System.out.print(j);
    i++; // Note: utilise i de la partie précédente
    if (j == 3) {
        j++;
    }
}
```

Qu'affiche le programme maintenant ?

a) 1 2 3 4 5 6 7 8 9 10 \\ 0 1 2
b) 1 2 3 4 6 7 8 9 10 \\ 0
c) 1 2 3 4 5 6 7 8 9 \\ 1 2 3
d) Le programme continue en boucle

-----

### Exercice 48

Quel est le résultat de la fonction suivante ?

```python
def mystery_function(a, b):
    if b == 0:
        return 1
    else:
        return a * mystery_function(a, b - 1)
```

a) $a \times b$
b) $a \times (b+1)$
c) $a^b$
d) $a^{b-1}$

-----

### Exercice 49

Soit le code suivant :

```python
film = {
    "titre": "Interstellar",
    "realisateur": {
        "prenom": "Christopher",
        "nom": "Nolan",
        "date" : 2014
    },
    "acteurs": [
        {"prenom": "Matthew", "nom": "McConaughey", "role": "Cooper"},
        {"prenom": "Anne", "nom": "Hathaway", "role": "Brand"},
        {"prenom": "Jessica", "nom": "Chastain", "role": "Murph"}
    ]
}

print(film["titre"])
print(film["realisateur"]["nom"] == "Nolan")

for acteurs in film["acteurs"] :
    print(acteurs["prenom"],acteurs["nom"])
```

Qu'affiche le code suivant ?

a) Interstellar True Matthew McConaughey Anne Hathaway Jessica Chastain
b) Interstellar True Matthew Cooper Anne Brand Jessica Murph
c) Inception True Matthew McConaughey Anne Hathaway Jessica Chastain
d) Interstellar False Cooper Brand Murph

-----

### Exercice 50

Quelle affirmation est vraie à propos du programme Java ci-dessous :

```java
public class SyntaxeError {
  public static void main(String[] args) {
    try {
        int x = 5  // omission volontaire du ;
    } catch (Exception e) {
        System.out.println("Erreur capturée");
        x = 5;
    }
  }
}
```

A) L'erreur de syntaxe est capturée par le bloc catch au moment de l'exécution, et le programme affiche "Erreur capturée".
B) L'erreur de syntaxe ne peut pas être capturée, et le programme plante au moment de l'exécution avec une SyntaxError.
C) Le programme ne compile pas à cause de l'erreur de syntaxe, donc il ne s'exécute jamais.
D) L'erreur de syntaxe est ignorée car elle est à l'intérieur d'un try-catch, et le programme s'exécute mais saute la déclaration de la variable.

-----

### Exercice 51

Soit le code ci-dessous en Python. Par quoi faut-il remplacer la ligne *\#ligne supprimée* dans la fonction `compatibilite(.)` pour qu’elle soit équivalente à la fonction `compatibiliteRapide(.)` ?

```python
def compatibilite(donneur, receveur):
  # modèle simplifié par rapport à la réalité !
  donneur_groupe = donneur[0]
  donneur_rhesus = donneur[1]
  receveur_groupe = receveur[0]
  receveur_rhesus = receveur[1]

  if donneur_rhesus == receveur_rhesus:
    if donneur_groupe == "O":
      return True
    elif receveur_groupe == "AB":
      return True
    elif donneur_groupe == receveur_groupe:
      return True
  return False

def compatibiliteRapide(donneur, receveur):
  #ligne supprimée
```

A) `return False`
B) `return donneur[0] == "O" or receveur[0] == "AB" or donneur[0] == receveur[0] and donneur[1] == receveur[1]`
C) `return (donneur[0] == "O" or receveur[0] == "AB" or donneur[0] == receveur[0]) or (donneur[1] == receveur[1])`
D) `return (donneur[0] == "O" or receveur[0] == "AB" or donneur[0] == receveur[0]) and (donneur[1] == receveur[1])`

-----

### Exercice 52

Soit le code suivant en Python, qu’est-ce qui sera affiché dans la console après son exécution ?

```python
complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
dna_strand = "ACTACT"
complementary_strand = ""
for base in dna_strand:
    complementary_strand += complements[base]
print(complementary_strand)
```

(A) ACTACT
(B) TGATGA
(C) AGTAGT
(D) KeyError 'ACTACT'

-----

### Exercice 53

Soit le code suivant en Python, qu’est-ce qui sera affiché dans la console après son exécution ?

```python
complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def comprev(dna):
    if len(dna) == 0:
        return ""
    return complements[dna[-1]] + comprev(dna[1:])

print(comprev("ACTACT"))
```

(A) TGATGA
(B) AGTAGT
(C) AAAAAA
(D) `RecursionError: maximum recursion depth exceeded`

-----

### Exercice 54

On souhaite écrire un programme qui vérifie si une équipe peut participer à un tournoi de sport selon les critères suivants :

  * Si l’équipe compte 3 membres, la moyenne d’âge doit être supérieure à 25.
  * Si l’équipe compte 2 membres, le ou la capitaine doit s’appeler "Alex".
  * Si l’équipe compte 1 membre, cette personne doit avoir 45 ans.

On dispose des variables suivantes :

  * `ages` : une liste d’entiers représentant les âges des membres de l’équipe.
  * `captainName` : une chaîne de caractères contenant le nom du ou de la capitaine.

Laquelle des lignes de code Python suivantes traduit correctement ces conditions ?

A) `(len(ages) == 3 and (ages[1] + ages[2] + ages[3])/3 > 25) or (captainName == "Alex" and len(ages) == 2) or (len(ages) == 1 and ages[1] == 45)`
B) `(len(ages) == 3 or (ages[0] + ages[1] + ages[2])/3 > 25) and (captainName == "Alex" or len(ages) == 2) and (len(ages) == 1 or ages[0] == 45)`
C) `(len(ages) == 3 and (ages[0] + ages[1] + ages[2])/3 > 25) or (captainName == "Alex" and len(ages) == 2) or (len(ages) == 1 and ages[0] == 45)`
D) `(len(ages) == 3 && (ages[1] + ages[2] + ages[3])/3 > 25) || (captainName == "Alex" && len(ages) == 2) || (len(ages) == 1 && ages[1] == 45)`

-----

### Exercice 55

Que va afficher l’exécution ?

```python
if __name__ == "__main__":
   def func1():
      i = 0
      value1 = 5
      value2 = 6
      def func2(value1, value2):
         global i
         i += 1
         value1 += 1
         value2 -= 1
         if i == 0:
            return value1
         else:
            return value2
      return func2(value1, value2) - func2(value1, value2)
   value1 = 3
   value2 = 4
   i = -1
   print(func1())
   i = 0
```

A) 5
B) 0
C) 1
D) Il y aura une erreur

-----

### Exercice 56

Supposons que l’on supprime les lignes 3, 16, 17 et 20 du code précédent. Quelle sera la conséquence sur l’exécution du programme ?

A) L’exécution donnera un résultat différent de la question précédente
B) L’exécution donnera le même résultat que la question précédente
C) On ne pourra pas exécuter car le code ne compilera pas
D) Une erreur sera provoquée

-----

### Exercice 57

En Python, quelle est la sortie du code suivant ?

```python
mon_tuple = (1,2,3)
print(4 in mon_tuple)
```

A. (1, 2, 3, 4)
B. True
C. False
D. (1, 2, 3)

-----

### Exercice 58

Que renverra ce code Java ?

```java
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
        for (int x : numbers) {
           System.out.println(x);
           if (x < 3) continue;
        }
    }
}
```

A. 1 2 3 4 5
B. 3 4 5
C. 1 2
D. Rien

-----

### Exercice 59

Quelles affirmations sont correctes concernant les deux programmes suivants :

```java
List<String> bonjour = List.of("Hello","Annyeong","Hola","Hallo","Arigato","Ciao","Salaam");

//Programme 1
LinkedList<String> bonjour2 = new LinkedList<>(bonjour);
Iterator<String> iter = bonjour2.iterator();
while(iter.hasNext()){
    String ling = iter.next();
    if(ling.charAt(0)=='H'){
        iter.remove();
    }
}
for (int i=0;i<bonjour2.size();i++){
    System.out.println(bonjour2.get(i));
}

//Programme 2
LinkedList<String> bonjour3 = new LinkedList<>(bonjour);
for (int i=0;i<bonjour3.size();i++){
    if(bonjour.get(i).charAt(0)!='H'){
        System.out.println(bonjour3.get(i));
    }
}
```

a) Les programmes afficheront la même chose
b) Le programme 1 provoque une erreur
c) Le programme 2 provoque une erreur
d) Le programme 1 modifie la liste "bonjour2"
e) Le programme 2 modifie la liste "bonjour3"

-----

### Exercice 60

Par quoi faut-il remplacer la ligne `#LINE REMOVED` pour que le programme suivant affiche la sortie ci-dessous :

```python
cars = {"nissan":["micra", "aryia"], "citroën":["picasso","cactus","C3"], "opel":["corsa"]}
for key in cars.keys():
    #LINE REMOVED
```

Sortie :

```text
nissan : ['micra', 'aryia']
citroën : ['picasso', 'cactus', 'C3']
opel : ['corsa']
```

a) `print("{} : {}".format(key,cars[key]))`
b) `print(key)`
c) `print("{} : {}".format(cars[1],cars.values[key]))`
d) `print("{} : {}".format("nissan", cars[key]))`
e) `print(cars)`

-----

### Exercice 61

Deux listes sont dites équivalentes si elles contiennent exactement les mêmes éléments, avec la même fréquence, sans que l’ordre importe.
On veut implémenter en Python une fonction récursive `equivalentes(l1, l2)` qui renvoie True si les listes l1 et l2 sont équivalentes.

```python
def equivalentes(l1, l2):
   if #Q2
      return True
   if len(l1) != len(l2):
      return False
   if l1[0] not in l2:
      return False
   l2_copy = l2.copy()
   l2_copy.remove(l1[0])
   #Q3
```

*(Voir questions suivantes pour Q2 et Q3)*

-----

### Exercice 62

Laquelle de ces propositions est fausse concernant le cas de base d’une fonction récursive ?

A) Le cas de base résout une partie du problème avant de poursuivre la récursion
B) Il représente la résolution du problème dans son cas le plus simple
C) Une fois arrivé au cas de base, nous pouvons remonter la pile (stack) d’appels pour obtenir notre réponse finale
D) Il permet dans certaines situations d’éviter un appel infini à la fonction elle-même

-----

### Exercice 63

Par quoi devons-nous remplacer `#Q2` pour bien représenter le cas de base dans notre contexte ?

A) `l1[0] == l2[0]:`
B) `len(l1) == 0 and len(l2) == 0:`
C) `l1 == l2:`
D) `len(l1) == 0 or len(l2) == 0:`

-----

### Exercice 64

Par quoi devons-nous remplacer `#Q3` pour que notre programme soit correct ?

A) `return equivalentes(l1, l2_copy)`
B) `return equivalentes(l1[1:], l2_copy)`
C) `return equivalentes(l1[1:], l2)`
D) `return equivalentes(l1[:len(l1)], l2[:len(l2)])`

-----

### Exercice 65

Imaginons que nous souhaitons vérifier si deux listes de nombres entiers sont équivalentes par itération. Laquelle de ces stratégies ne fonctionnerait pas ? (On suppose que les deux listes ont la même taille).

A) Pour chaque élément de l1, on vérifie si cet élément est contenu dans l2.
B) On crée un dictionnaire qui associe à chaque élément de l1 son nombre d’apparitions ; pour chaque élément de l2, on vérifie que c’est une clé du dictionnaire et que la valeur correspond à son nombre d’apparitions dans l2.
C) Pour chaque élément de l1, on vérifie s’il apparaît le même nombre de fois dans l1 et l2.
D) On réarrange chaque liste dans l’ordre croissant, puis on compare indice par indice du début à la fin.

-----

### Exercice 66

Qu'affiche le code suivant (Python) ?

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for x in numbers:
    if x < 6:
        numbers.remove(x)
print(numbers)
```

a. [6, 7, 8]
b. [2, 4, 6, 7, 8]
c. [1, 3, 5, 6, 7, 8]
d. RuntimeError: list changed size during iteration

-----

### Exercice 67

On souhaite supprimer toutes les entrées dont la valeur est inférieure à 0. La variable suivante est donnée :

```java
Map<String, Integer> scores = new HashMap<>();
scores.put("a", 3);
scores.put("b", -1);
scores.put("c", 0);
scores.put("d", -5);
```

Laquelle de ces versions ne provoque pas d’exception et produit le résultat attendu ?

A.

```java
for (String key : scores.keySet()) {
    if (scores.get(key) < 0) {
        scores.remove(key);
    }
}
```

B.

```java
for (Map.Entry<String, Integer> e : scores.entrySet()) {
    if (e.getValue() < 0) {
        scores.remove(e.getKey());
    }
}
```

C.

```java
Iterator<Map.Entry<String, Integer>> it = scores.entrySet().iterator();
while (it.hasNext()) {
    if (it.next().getValue() < 0) {
        it.remove();
    }
}
```

D.

```java
Iterator<String> it = scores.keySet().iterator();
while (it.hasNext()) {
    String k = it.next();
    if (scores.get(k) < 0) {
        scores.remove(k);
    }
}
```

-----

### Exercice 68

Qu'affiche le code suivant (Python) ?

```python
def mystery(n, acc=[]):
    if n == 0:
        return acc
    acc.append(n)
    return mystery(n - 1)
a = mystery(3)
b = mystery(2)
print(a, b)
```

a. [3, 2, 1] [2, 1]
b. [3, 2, 1] [3, 2, 1]
c. [3, 2, 1, 2, 1] [3, 2, 1, 2, 1]
d. Provoque une erreur (RecursionError)

-----

### Exercice 69

En Java, quel code définit correctement un getter pour un attribut privé `type` ?

A. `public void getType() { return type; }`
B. `private String getType() { return this.type; }`
C. `public String getType() { return type; }`
D. `public static String getType() { return type; }`

-----

### Exercice 70

En Java, quelle est la syntaxe correcte pour indiquer qu’une classe `Voiture_Electrique` hérite de `Voiture` ?

A. `class Voiture_Electrique -> Voiture`
B. `class Voiture_Electrique extends Voiture`
C. `class Voiture_Electrique inherits Voiture`
D. `class Voiture_Electrique super Voiture`

-----

### Exercice 71

Soit la classe suivante. Écrivez le code de la fonction `canPlay`.
Deux chats ne veulent pas jouer ensemble si le mood de l'un des deux est inférieur (strictement) à 3, dans ce cas la fonction retourne faux, sinon elle retourne vrai.

```java
public class Cat {
    public String name;
    private int age;
    private int mood = 5;
    // ... constructeurs et setters ...
    public boolean canPlay(Cat otherCat){
        // ???
    }
}
```

-----

### Exercice 72

Compléter le code suivant en ajoutant l'attribut nécessaire à la ligne 1 et compléter le constructeur à la ligne 2 et 3.

```java
public class Animal {
    private String type;
    protected String name;
    protected int age;
    protected int nb_animal = 0;
    public Animal(String type, String name, int age){
        this.type = type;
        this.name = name;
        this.age = age;
    }
}

public class Cat extends Animal {
    // Ligne 1
    public Cat(String name, int age, String type, int mood) {
        // Ligne 2
        // Ligne 3
    }
    // ...
}
```

-----

### Exercice 73

Soit la suite $U_n$ donnée par $U_0 = 4$ et $\forall n > 1, U_n = n + U_{n-1}^2$.

```python
def suite(n):
  if n == 0:
    return ???
  else:
    return ???
```

Par quoi faut-il remplacer les `???` pour que le code fonctionne ?

a) 4 et `n + suite(n+1)`
b) 0 et `n + u(n-1)**2`
c) 4 et `n + suite(n-1)**2`
d) 0 et `n**2 + suite(n+1)`

-----

### Exercice 74

Quelle sera la sortie dans la console après l'exécution du programme `CoffeeShop` ?

```java
// Fichier: CoffeeMachine.java
public class CoffeeMachine {
  public static int coffeesMadeCount = 0;
  public CoffeeMachine() {}
  public void makeCoffee() {
      CoffeeMachine.coffeesMadeCount++;
  }
}

// Fichier: CoffeeShop.java
public class CoffeeShop {
  public static void main(String[] args) {
    CoffeeMachine machine1 = new CoffeeMachine();
    CoffeeMachine machine2 = new CoffeeMachine();
    machine1.makeCoffee();
    System.out.println(machine1.coffeesMadeCount);
    machine2.makeCoffee();
    System.out.println(machine2.coffeesMadeCount);
    CoffeeMachine.coffeesMadeCount = 0;
    System.out.println(machine1.coffeesMadeCount);
    }
}
```

A. 1 / 1 / 0
B. 1 / 2 / 0
C. 1 / 1 / 1
D. 1 / 2 / 1

-----

### Exercice 75

Comment empêcher le `CoffeeShop` de réinitialiser l'attribut `CoffeesMadeCount`, tout en laissant le `CoffeeShop` consulter la valeur de l'attribut ? (Sélectionnez toutes les modifications nécessaires).

A) Rendre `CoffeesMadeCount` privée
B) Créer un getter pour `CoffeesMadeCount`
C) Créer un setter pour `CoffeesMadeCount`
D) Supprimer le mot-clé `static` de `CoffeesMadeCount`

-----

### Exercice 76

Sélectionnez les affirmations correctes :

A) En Java, les attributs d'une classe peuvent être initialisés directement lors de leur déclaration, en dehors de tout constructeur.
B) En Python, des attributs propres à chaque instance peuvent être déclarés en dehors de toute méthode (dans le corps de la classe).
C) En Python, la référence à l'instance (self) doit être passée explicitement comme premier argument de chaque méthode d'instance, contrairement au mot-clé this en Java qui est implicite.
D) En Python, le constructeur d'une classe est défini par la méthode spéciale `__init__`, alors qu'en Java, il porte le même nom que la classe.

-----

### Exercice 77

Qu'affiche le programme suivant ?

```python
class Logger:
    def __init__(self):
        self.events = []
    def log(self, msg):
        self.events.append(msg)
    def summary(self):
        return "-".join(self.events)

class Process(Logger):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def start(self):
        self.log("start:" + self.name)
        self.execute()
    def execute(self):
        self.log("exec:" + self.name)
    def stop(self):
        self.log("stop:" + self.name)

class TimedProcess(Process):
    def __init__(self, name, ticks):
        super().__init__(name)
        self.ticks = ticks
    def execute(self):
        for i in range(self.ticks):
            self.log(f"tick{i}")
        super().execute()
        self.stop()

p = TimedProcess("P1", 2)
p.start()
print(p.summary())
```

a. `start:P1-tick0-tick1-stop:P1`
b. `tick0-tick1-start:P1-exec:P1-stop:P1`
c. `start:P1-tick0-tick1-exec:P1-stop:P1`
d. Ce programme n'affiche rien.

-----

### Exercice 78

Quelle est la sortie de ce code ?

```java
class Enseignant {
    protected int baseSalary = 3000;
    public int salaireMensuel() { return baseSalary; }
}
class Professeur extends Enseignant {
    private int committees;
    public Professeur(int committees) { this.committees = committees; }
    public int salaireMensuel() { return super.salaireMensuel() + committees * 200; }
}
class Collaborateur extends Enseignant {
    private int hours, rate;
    public Collaborateur(int hours, int rate) { this.hours = hours; this.rate = rate; }
    public int salaireMensuel() { return hours * rate; }
}

public class Test {
    public static void main(String[] args) {
        Enseignant e = new Professeur(3);
        Enseignant f = new Collaborateur(10, 50);
        System.out.println(e.salaireMensuel() + f.salaireMensuel());
        e = f;
        System.out.println(e.salaireMensuel());
    }
}
```

a. 4100 / 500
b. 3500 / 3000
c. 4100 / 3000
d. 3000 / 500

-----

### Exercice 79

Laquelle des affirmations suivantes est vraie ?

a. L’héritage permet à une sous-classe d’accéder directement aux champs private de sa superclasse.
b. L’encapsulation vise à cacher la complexité interne d’un objet, permettant de l’utiliser uniquement via les méthodes définies dans sa classe.
c. La modularisation consiste à regrouper dans une seule classe toutes les fonctionnalités nécessaires au programme pour éviter la duplication de code.
d. Le sous-typage empêche une instance d’une sous-classe d’être utilisée là où un objet de la classe mère est attendu.

-----

### Exercice 80

Soit le code ci-dessous, par quoi faut-il remplacer les `???` pour que le code fonctionne ?

```python
class Circle:
    def __init__(self,rayon):
        self.__rayon = rayon
    def get_rayon(self):
        return self.__rayon
    def __eq__(self, other):
        if ???:
            if self.__rayon == self.get_rayon():
                return True
            else:
                return False
  else:
    return False
```

a) `isinstance(other, Circle)`
b) `isinstance(other,self)`
c) `other.isCircle()`
d) `other.equal(Circle)`

-----

### Exercice 81

Qu'affiche le code ci-dessous ?

```python
counter = 0
class Vehicle:
    def __init__(self, brand):
        global counter
        counter += 1
        self._id = counter
        self._brand = brand
    def start(self):
        print("Starting vehicle-" + str(self._id))
        self.engine()
    def engine(self):
        print("- generic engine started")
class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors
    def start(self):
        print("Starting car-" + str(self._id) +" " + self._brand)
        super().start()
    def engine(self):
        print("- car engine with " + str(self.doors) + " doors started")
vehicle = Car("Toyota", 4)
vehicle.start()
vehicle = Vehicle("Generic")
vehicle.start()
```

*(Plusieurs choix de sortie sont possibles, voir énoncé)*

-----

### Exercice 82

Laquelle des phrases suivantes est fausse concernant les attributs ?

a) le mot clé `static` en java désigne un attribut de classe
b) `__attribut` désigne un attribut privé en python
c) un getter est nécessaire pour utiliser un attribut privé d'un objet sur lequel une méthode est appelée
d) le mot clé `self` est nécessaire pour utiliser un attribut d'un objet sur lequel une méthode est appelée en java

-----

### Exercice 83

Les trois classes java suivantes sont définies (Vehicle, Car, Bike). Quelle ligne ne provoque aucune erreur ?

a) `vehicle train = new vehicle("train", 100, 30.6);`
b) `vehicle jeep = new car("jeep",140,false);`
c) `bike kawa = new bike("kawa", 300,true);`
d) `car lambo = new vehicle("lambo",500,4);`

-----

### Exercice 84

Parmi les expressions suivantes, lesquelles rendent `true` lorsque les objets a et b ont les mêmes attributs et sous quelle condition ?

a. `a.equals(b)` (sans condition particulière)
b. `a.equals(b)` (si la méthode equals() est redéfinie dans ce but)
c. `a == b` (si a et b sont de type int)
d. `a == b` (si on a assigné la valeur a à b ou l'inverse)
e. aucune de ces réponses

-----

### Exercice 85

Soit la classe suivante en Java :

```java
public class car extends vehicle {
    private int  nb_seats;
    public boolean isOpenRoof;
    private static float nb_mini;
    public double height;
    // constructeur...
}
```

A. les attributs name et speed peuvent être définis comme privés ou publics dans la classe mère
B. la valeur par défaut de OR est false
C. les attributs nb\_seats et nb\_mini sont privés
D. les attributs nb\_mini et height sont de même type
E. l'attribut nb\_mini est un attribut de classe
F. la classe mère définit exactement deux attributs

-----

### Exercice 86

Quelle réponse correspond à la ligne manquante ?

```python
class Person:
    def __init__(self, name):
        #LINE REMOVED
p = Person("Alice")
print(p.name)
```

A) `self.name = name`
B) `name = self.name`
C) `return name`
D) `print name`

-----

### Exercice 87

Quel sera le résultat affiché par le programme ?

```python
class Compteur:
    def __init__(self, valeur):
        self.valeur = valeur
    def ajouter(self, x):
        self.valeur += x

class Multiplicateur:
    def __init__(self, facteur):
        self.facteur = facteur
    def multiplier(self, x):
        return x * self.facteur

c = Compteur(5)
m = Multiplicateur(3)
c.ajouter(2)
resultat = m.multiplier(c.valeur)
print(resultat)
```

A) 15
B) 21
C) 17
D) 7

-----

### Exercice 88

Étant donné que cet extrait de code compile et s'exécute avec succès, quelles affirmations suivantes pourraient décrire avec précision la relation entre Node, File et Folder ?

```java
Node node1 = new File("document.txt", 1024);
Node node2 = new Folder("My Documents");
List<Node> nodes = new ArrayList<>();
nodes.add(node1);
nodes.add(node2);
```

A) Node est une interface, et File et Folder sont des classes qui implémentent Node
B) Node est une classe abstraite, et File et Folder sont des classes qui étendent Node
C) Node est une classe concrète (non abstraite), et File et Folder sont des classes qui étendent Node
D) File est une classe, et Node et Folder sont des classes qui étendent File
E) Node, File et Folder sont trois classes qui n'ont aucun lien de parenté.

-----

### Exercice 89

Cochez les affirmations correctes :

1.  Une classe Java peut implémenter plusieurs interfaces.
2.  Une classe Java peut étendre plusieurs classes.
3.  Une classe fille peut accéder aux attributs privés de la classe mère.
4.  Une classe déclarée abstract ne peut pas avoir de constructeur.

-----

### Exercice 90

Soit `Animal a = new Chien();` (où `Chien extends Animal`). Si Animal et Chien ont tous deux une méthode `manger()`, laquelle sera appelée par `a.manger()` ?

1.  Celle de la classe Animal
2.  Le code ne compile pas car a est de type Chien
3.  Le code ne compile pas car a est de type Animal
4.  Celle de la classe Chien

-----

### Exercice 91

Laquelle de ces affirmations concernant la classe HalloweenParty est vraie ? (Voir spécifications ci-dessus)

A) On peut accéder à l’attribut costumes depuis une instance de la classe HalloweenParty
B) La méthode getCostume peut accéder à l’attribut costumes
C) `new HalloweenParty(Map.of("John", "Shrek", "Alicia", "Batman"))` ne lèvera pas d’erreurs
D) Après avoir instancié HalloweenParty, si on appelle getCostume avec un nom qui n’est pas une clef de costumes, cela lèvera une erreur

-----

### Exercice 92

Laquelle de ces implémentations satisfait la description de la méthode `addPerson` ?
*(Voir options dans l'énoncé source)*

-----

### Exercice 93

Pourquoi la méthode `isCostumeTaken` est-elle déclarée private ?

A) Parce qu’elle renvoie un booléen.
B) Parce qu’elle peut lancer des exceptions.
C) Parce qu’on souhaite qu’elle soit accessible en dehors de la classe
D) Parce qu’elle ne doit être utilisée que comme méthode interne à la classe, pour faciliter l’ajout de personnes.

-----

### Exercice 94

Qu’affichera l’exécution suivante ?

```java
HalloweenParty hp = new HalloweenParty();
hp.addPerson("Richard", "Dinosaur");
hp.addPerson("Nancy", "Dinosaur");
hp.addPerson("Richard", "Pilot");
System.out.println("Richard will be dressed as: " + hp.getCostume("Richard"));
```

*(Voir les options dans l'énoncé source)*

-----

### Exercice 95

Considérons le code Java suivant sur la classe Person. Quel sera le résultat affiché ?

```java
Person p1 = new Person("Ted", "Mosby");
Person p2 = new Person("Ted", "Mosby");
System.out.println((p1 == p2));
System.out.println(p1.equals(p2));
```

a. true / true
b. false / true
c. true / false
d. false / false

-----

### Exercice 96

Parmi les affirmations suivantes, laquelle(s) est/sont correcte(s) ?

a. Une classe abstraite définit un type et fournit une implémentation partielle.
b. Une interface Java peut contenir du code exécuté, au même titre qu’une classe concrète.
c. En Java, une classe peut hériter de plusieurs classes mais d’une seule interface.
d. En Python, les notions de type, classe et interface sont moins strictement différenciées à cause de l’absence de typage statique.

-----

### Exercice 97

Quel est l’intérêt de rendre une classe abstraite ? (Plusieurs bonnes réponses possibles)

A) Cela rend son instanciation impossible
B) Permettre de revenir implémenter la classe plus tard
C) Assurer que toutes les classes filles auront la même implémentation des méthodes abstraites
D) Mettre en place une structure commune pour ses classes filles

-----

### Exercice 98

Aurions-nous eu une erreur si on retirait l’implémentation de `getDescription` dans `TennisTournament` (qui hérite de `Tournament` abstrait) ?

A) Oui, car la classe mère est abstraite, et il faut implémenter chaque méthode
B) Non, car nous avons déjà une implémentation dans la classe mère
C) Oui, car le type de retour de la fonction est String
D) Non, car on peut implémenter une classe comme on le souhaite

-----

### Exercice 99

Aurions-nous eu une erreur si on retirait l’implémentation de `getTournamentType` dans `BasketballTournament` ?

A) Oui, car la classe mère est abstraite, et il faut implémenter chaque méthode
B) Non, car le @Override indique qu’elle peut être retirée
C) Oui, car la méthode est abstraite dans la classe mère
D) Non, car on peut implémenter une classe comme on le souhaite

-----

### Exercice 100

Qu’affichera ce programme (Main Tournament) à l’exécution ?

A) Ce programme va lever une erreur
B) Tournament 1: This tournament has 32 teams.
C) Tournament 1: Basketball tournament. This tournament has 32 teams. Each quarter lasts 10 minutes. / Tournament 2: Tennis tournament. This tournament has 128 teams. This tournament is a Grand Slam.
D) Autres options...

-----

### Exercice 101

Comment pourrais-je accéder à l’attribut `quarterDurationMinutes` de `tournament1` (déclaré comme Tournament) ?

A) Il faut faire un type casting
B) Il n’est pas possible d’accéder à cet attribut
C) Il faut implémenter un getter dans la classe Tournament
D) `tournament1.quarterDurationMinutes`

-----

### Exercice 102

Quelle est la forme simplifiée de l’expression suivante ?
$(p \land q) \lor (\neg p \land q) \lor (p \land r)$

A. $q \lor (p \land r)$
B. $p \lor q \lor r$
C. $q \lor r$
D. $q$

-----

### Exercice 103

Soit le code Java ci-dessous. Par quelle instruction faut-il remplacer la ligne `#LINE REMOVED` pour que les deux fonctions renvoient le même résultat ?

```java
public static boolean test1(int x){
    if (x % 4 == 0) return true;
    else if (x % 2 == 0) return false;
    else return true;
}
public static boolean testAlt(int x){
    #LINE REMOVED
}
```

A. `return (x % 4 == 0) || (x % 2 != 0);`
B. `return (x % 4 == 0) && (x % 2 != 0);`
C. `return (x % 4 != 0) || (x % 2 == 0);`
D. `return (x % 4 != 0) && (x % 2 == 0);`

-----

### Exercice 104

Which of the following correctly represents the number 5 in set theory?

a. `{∅,{∅},{∅,{∅}},{∅,{∅},{∅,{∅}}}}`
b. ` {∅,{∅},{∅,{∅}},{∅,{∅},{∅,{∅}}},{∅,{∅},{∅,{∅}},{∅,{∅},{∅,{∅}}}}}  `
c. `{{∅},{∅,{∅}},{∅,{∅,{∅}}}}`
d. `{∅,{∅,{∅,{∅,{∅}}}}}`

-----

### Exercice 105

Considérons le diagramme de Venn suivant, dans lequel A, B, C, D et F représentent des sous-ensembles de E, et où a, b, c, d, e, f, g, h, i sont des éléments de E. Parmi les assertions suivantes, laquelle(s) est/sont correcte(s) ?

-----

### Exercice 106

Combien de sous-ensembles contient l'ensemble E = {1,2,3,4}

a) 4
b) 8
c) 16
d) 32

-----

### Exercice 107

Dans quels cas la proposition suivante est vraie ?
$(((P \land Q) \lor P) \land (\neg Q \land Q)) \lor (\neg P \land Q) \lor (P \lor Q)$

a) P=V, Q=V
b) P=V, Q=F
c) P=F, Q=V
d) P=F, Q=F
e) Aucune de ces réponses

-----

### Exercice 108

Laquelle de ces propositions est vraie par rapport à la classe (java) qui débute par la ligne de code suivante : `public abstract class Country{`

a) C'est une interface
b) Elle peut être instanciée
c) Elle peut hériter d'une autre classe si le nom est suivi du mot-clé implements
d) Elle peut contenir des méthodes abstraites

-----

### Exercice 109

Considérez le code suivant. Quelle est sa complexité ?

```python
def boucle(n):
    k = 0
    for i in range(n):
        for j in range(100):
            k += 1
    return k
```

A. O(log n)
B. O(n)
C. O(n²)
D. O(1)

-----

### Exercice 110

Considérez le code suivant. Quelle est sa complexité ?

```python
def boucle(n):
    k = 0
    for i in range(n):
        for j in range(i):
            k += 1
    return k
```

A. O(n²)
B. O(n)
C. O(n log n)
D. O(log n)

-----

### Exercice 111

[Image of O(log n) complexity graph]

Considérez le code suivant. Quelle est sa complexité ?

```python
i = 1
while i < n:
    for j in range(n):
        print(i, j)
    i = i * 2
```

A. O(n²)
B. O(n)
C. O(n log n)
D. O(log n)

-----

### Exercice 112

Quelle est la complexité de la fonction suivante en java ?

```java
public static void fonction(String word,int number) {
   int n = word.length()-1;
   while (n >= 0) {
       for (int i=0;i<number;i++) {
           System.out.println(word.charAt(n));
       }
       n--;
   }
}
```

a) O(n)
b) O(n²)
c) O(n\*m)
d) O(n+m)

-----

### Exercice 113

En appliquant la fonction merge\_sort() telle que vue en cours sur la liste suivante `[9,6,2,4,5,8]`, quelle est la paire de sous-listes sur laquelle `merge()` ne sera à aucun moment appelé ?

a) [6] et [2]
b) [2, 6, 9] et [4, 5, 8]
c) [4] et [5, 8]
d) [2] et [4]

-----

### Exercice 114

Comment modifier tri-fusion pour que la liste soit triée par ordre décroissant :

A) Inverser la liste avant de commencer le tri.
B) Changer l'ordre des appels récursifs.
C) Modifier le signe de comparaison dans l'étape de fusion.
D) Aucune de ces réponses.

-----

### Exercice 115

Combien de fois la fonction `merge` va être appelée lors du tri-fusion sur une liste de $n$ éléments ?

A) $n$ fois
B) $n-1$ fois
C) $\log_2(n)$
D) Cela dépend de la parité de la liste
E) Aucune de ces réponses.

-----

### Exercice 116

Quelle est la modification la plus efficace pour correctement supprimer les doublons de la liste pendant son tri avec tri-fusion.

A) Trier normalement, puis parcourir la liste finale pour retirer les éléments identiques.
B) Vérifier si l'élément existe déjà dans la liste complète avant chaque insertion.
C) Si les deux éléments comparés sont égaux, n'en ajouter qu'un seul au résultat et avancer les deux indices.
D) Aucune de ces réponses

-----

### Exercice 117

Les affirmations suivantes sont données :

  * Si Alice prend un dessert, Bob en prend un aussi.
  * Chaque jour, soit Bob, soit Cathy, mais jamais les deux, prend un dessert.
  * Alice ou Cathy, ou les deux, prennent chaque jour un dessert.
  * Si Cathy prend un dessert, Alice fait de même.

Quelle combinaison de personnes prend un dessert si toutes les affirmations sont vraies ?

a) Alice seulement
b) Bob seulement
c) Cathy seulement
d) Alice et Bob uniquement

-----

### Exercice 118

Dans un ensemble E, considérons trois parties A, B, C. On sait que :
$\{h, b\} \subset \bar{A} \cap \bar{B}$
$\{a, f\} \subset A \cup C$

Laquelle des propositions suivantes est vraie ?

a) $h \in A$
b) $b \in B$
c) $a \in A \cup C$
d) $f \notin C$

-----

### Exercice 119

Une classe abstraite en Java :

a) Peut être instanciée directement
b) Doit obligatoirement contenir au moins une méthode abstraite
c) Peut contenir des méthodes abstraites ou non
d) Ne peut pas contenir d’attributs

-----

### Exercice 120

Dans une interface Java :

a) Les méthodes sont private par défaut
b) Les méthodes sont public abstract par défaut
c) Les variables sont privées par défaut
d) Les variables ne peuvent pas être finales

-----

### Exercice 121

Quelle est la bonne séquence d’étapes du tri fusion ?

a) Fusionner toute la liste / Diviser en deux moitiés / Trier séparément / Arrêter
b) Diviser la liste en deux moitiés / Diviser encore chaque moitié jusqu’à obtenir des listes de taille 1 / Fusionner les petites listes pour former des listes triées / Continuer les fusions jusqu’à obtenir une seule liste triée
c) Trouver le plus petit élément / Le placer au début / Répéter pour le second plus petit, etc. / Arrêter
d) Trier d’abord la moitié droite / Trier ensuite la moitié gauche / Coller les deux moitiés sans les comparer / Arrêter

-----

### Exercice 122

Soit le code suivant. Quelle est la complexité de cet algorithme si la liste L contient n éléments ?

```python
def multiply(L):
    total = 1
    for x in L:
        total = total * x
    return total
```

a) O(1)
b) O(log n)
c) O(n)
d) O(n²)

-----

### Exercice 123

Quelle condition impérative une collection doit-elle respecter pour qu'on puisse y appliquer une recherche binaire (Binary Search) ?

A. Elle doit être triée.
B. Elle doit être stockée dans une liste chaînée.
C. Elle ne doit pas contenir de doublons.
D. Elle doit contenir uniquement des entiers.

-----

### Exercice 124

Soit un arbre de recherche binaire vide dans lequel on insère la séquence suivante : `{47,23,89,11,37,73,97}`. Si on insère ensuite la valeur 31, où atterrit-elle ?

A. Comme enfant droit de 11.
B. Comme enfant gauche de 73.
C. Comme enfant gauche de 37.
D. Comme enfant droit de 23.