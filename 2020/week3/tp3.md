Algorithmes et Pensée Computationnelle
======================================

# Programmation de base

Le but de cette séance est d'aborder des notions de base en programmation. Au terme de cette séance, l'étudiant sera capable de:
- définir une variable, de définir son type et sa valeur.
- Définir une fonction et comprendre son rôle.
- Utiliser des notions d'algèbre booléenne.
- Comprendre la notion d'entrée/sortie.
Les langages qui seront utilisés pour cette séance sont __Java__ et __Python__. Assurez-vous d'avoir bien installé __Pycharm__ et __Netbeans__. Si vous rencontrez des difficultés, n'hésitez pas à vous référer au guide suivant: ** tutoriel d'installation des outils et prise en main de l'environnement de travail **.


## Exercice 1: Représentation de nombres entier

**Question 1: Unsigned int (5 min)** 

  Sur 8 bit écrire 113<sub>10</sub> en base binaire.

  **Hint:** Faire un tableau comme présenté dans le cours page 9 de la semaine 3. Essayer de décomposer en une somme de puissances de 2 le nombre.

  **Solution:** 
  1. Décomposer le nombre en une somme de puissances de 2.

  113 = 64 + 32 + 16 + 1 = 1 * 2<sup>6</sup> + 1 * 2<sup>5</sup> + 1* 2<sup>4</sup> + 1 * 2<sup>0</sup>

  2.  Inclure les coefficients dans un tableau:

  | 2<sup>7</sup> | 2<sup>6</sup> | 2<sup>5</sup> | 2<sup>4</sup> | 2<sup>3</sup> | 2<sup>2</sup> | 2<sup>1</sup> | 2<sup>0</sup> |
  | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
  | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |

  Donc la représentation en binaire de l'entier non signé 113 est: 01110001


**Question 2: Signed integers with signed magnitude (2 min)**

  En utilisant le résultat de la question précédente, écrire sur 8 bit -113<sub>10</sub> en base binaire 

  **Hint:** Pour cette représentation, on réserve le 7ème bit pour le signe.

  **Solution:**

  | 2<sup>7</sup> | 2<sup>6</sup> | 2<sup>5</sup> | 2<sup>4</sup> | 2<sup>3</sup> | 2<sup>2</sup> | 2<sup>1</sup> | 2<sup>0</sup> |
  | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
  | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |

  Donc l'expression de -113 en utilisant la méthode de "signed integers" est 11110001

**Question 3: Complément à 1 (5 min)** 

  Ecrire le complément à 1 de -113<sub>10</sub>. 

  Qu'elle est la différence entre cette méthode par rapport à celle précédente ?

  **Hint:** 

  1. En programmation l'opposé d'une variable est not( la variable). Ici, le même principe s'applique. L'opposé de 0 en binaire est...
  2. Comment peut-on exprimer 0 dans cette méthode ?



  **Solution:** 
  1.

  | 2<sup>7</sup> | 2<sup>6</sup> | 2<sup>5</sup> | 2<sup>4</sup> | 2<sup>3</sup> | 2<sup>2</sup> | 2<sup>1</sup> | 2<sup>0</sup> |
  | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
  | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |
  | not | not | not | not | not | not | not | not |
  | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 |

  2. La portée de cette méthode ne change pas par rapport à celle précédente. Par contre, l'expression de -0 sera différente. 

  **Signed magnitude:** -0<sub>10</sub> = 10000000<sub>2</sub>

  **Complément à 1:** -0<sub>10</sub> = 11111111<sub>2</sub>

  Both have the same range: range = [-127<sub>10</sub>,+127<sub>10</sub>] 


**Question 4: Complément à 2 (5 min)**
  
  Quel est le complément à 2 de -113<sub>10</sub> ?
  
  Quelle est l'utilitée de cette représentation ?
  
  **Hint:** Chaque représentation est-elle unique ?
  
  **Solution:** 
  
  1. Il faut ajouter un au complément à 1 de -113<sub>10</sub>. C'est à dire faire plus un à la colonne de 2<sup>0</sup>.
  
  | 2<sup>7</sup> | 2<sup>6</sup> | 2<sup>5</sup> | 2<sup>4</sup> | 2<sup>3</sup> | 2<sup>2</sup> | 2<sup>1</sup> | 2<sup>0</sup> |
  | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
  | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |
  
  2. Il n'y a plus qu'une représentation possible pour -0<sub>10</sub>. Il y'a donc un nombre de plus possible par rapport aux dernières représentations. La      nouvelle range est donc: range = [-128<sub>10</sub>,+127<sub>10</sub>] 
  
 **Question 5: Floating point ( 10 min)**
  
  Que vaut en base 10 le chiffre binaire suivant d'après la représentation floating point ?
  
  | Sign | Exponent | Mantissa |
  | --------- | --------- | --------- | 
  | 0 | 00110101 | 01000001000000000000001 |
  
  **Hint:** Poser chaque calcul, et ensuite tout fusionner avec la formule. Utilisez la page 14 de la semaine 3 comme exemple.
  
  **Solution:**
  
  *sign* = 0 --> (-1)<sup>sign</sup> = (-1)<sup>0</sup> = 1
  
  *e* = exponent = exponent = 0 * 2<sup>7</sup> + 0 * 2<sup>6</sup> + 1 * 2<sup>5</sup> + 1 * 2<sup>4</sup> + 0 * 2<sup>3</sup> + 1 * 2<sup>2</sup> + 0 * 2<sup>1</sup> + 1 * 2<sup>0</sup> = 53
  
  *2<sup>e-127</sup>* = 2<sup>53-127</sup> = 2<sup>-74</sup>
  
  mantissa = 01000001000000000000001 = 1 + 0 * 2<sup>-1</sup> + 1 * 2<sup>-2</sup> + 0 * 2<sup>-3</sup> + (...) + 1 * 2<sup>-8</sup> + 1 * 2<sup>-23</sup> = 
  
  Donc Valeur = (+1) * mantissa
