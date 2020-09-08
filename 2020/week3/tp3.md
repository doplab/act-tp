Algorithmes et Pensée Computationnelle
======================================

# Programmation de base

Le but de cette séance est d'aborder des notions de base en programmation. Au terme de cette séance, l'étudiant sera capable de:
- définir une variable, de définir son type et sa valeur.
- Définir une fonction et comprendre son rôle.
- Utiliser des notions d'algèbre booléenne.
- Comprendre la notion d'entrée/sortie.
Les langages qui seront utilisés pour cette séance sont __Java__ et __Python__. Assurez-vous d'avoir bien installé __Pycharm__ et __Netbeans__. Si vous rencontrez des difficultés, n'hésitez pas à vous référer au guide suivant: ** tutoriel d'installation des outils et prise en main de l'environnement de travail **.


## Exercice 1: Représentation de nombres entier ( 30 minutes)

**Question 1: Entiers non signés ( 5 minutes)** 

  Sur 8 bits écrire (113)<sub>10</sub> en base binaire.

  **Hint:** 
  
  * Faire un tableau comme présenté dans le cours page 9 de la semaine 3. Essayer de décomposer en une somme de puissances de 2 le nombre.

  **Solution:** 
  1. Décomposer le nombre en une somme de puissances de 2.

  113 = 64 + 32 + 16 + 1 = 1 * 2<sup>6</sup> + 1 * 2<sup>5</sup> + 1* 2<sup>4</sup> + 1 * 2<sup>0</sup>

  2.  Inclure les coefficients dans un tableau:

  | 2<sup>7</sup> | 2<sup>6</sup> | 2<sup>5</sup> | 2<sup>4</sup> | 2<sup>3</sup> | 2<sup>2</sup> | 2<sup>1</sup> | 2<sup>0</sup> |
  | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
  | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |

  Donc la représentation en binaire de l'entier non signé (113)<sub>10</sub> est: (01110001)<sub>2</sub>


**Question 2: Entiers signés négatifs ( 2 minutes)**

  En utilisant le résultat de la question précédente, écrire sur 8 bits -113<sub>10</sub> en base binaire.

  **Hint:** 
  
  * Pour cette représentation, on réserve le 7ème bit pour le signe. 
 
  * Le bit vaut 0 pour un nombre positif et 1 pour un nombre négatif.
  

  **Solution:**

  | 2<sup>7</sup> | 2<sup>6</sup> | 2<sup>5</sup> | 2<sup>4</sup> | 2<sup>3</sup> | 2<sup>2</sup> | 2<sup>1</sup> | 2<sup>0</sup> |
  | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
  | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |

  Le tableau doit être lu de droite à gauche
  
  Donc l'expression de (-113)<sub>10</sub> en utilisant la représentation d'entiers signés est (11110001)<sub>2</sub>.
  

**Question 3: Complément à 1 ( 5 minutes)** 

  Ecrire le complément à 1 de -113<sub>10</sub>. 

  Qu'elle est la différence entre cette méthode par rapport à la précédente ?

  **Hint:** 
 
  1. En programmation l'opposé d'une variable est not( la variable). Ici, le même principe s'applique. L'opposé de 0 en binaire est 1. 
  2. Pour étudier la différence, il faut regarder les différenttes manières d'exprimer -0 en binaire ( se référer à la page 10 de la semaine 3).



  **Solution:** 
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


**Question 4: Complément à 2 ( 3 minutes)**
  
  Quel est le complément à 2 de (-113)<sub>10</sub> ?
  
  Quelle est l'utilitée de cette représentation ?
  
  **Hint:** 
  
 1. Voici l'exemple du cours expliqué étape par étape:
 
  | Chiffre | bit 7 | bit 6 | bit 5 | bit 4 | bit 3 | bit 2 | bit 1 | bit 0 |
  | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
  | (87)<sub>10</sub> | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 1 |    # Cette étape est la conversion d'un entier positif de base 10 en base 2.
  | (-87)<sub>10</sub> | not | not | not | not | not | not | not | not |  # Comme pour le complément à 1 on prend l'opposé de chaque bit.
  | (-87)<sub>10</sub> | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |    # On ajoute 1 au bit 0 pour passer à l'étape d'après qui est le complément à 2 de (-87)<sub>10</sub>
  | (-87)<sub>10</sub> | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
  | (-87)<sub>10</sub> | (-1) * 2<sup>7</sup> | 0 * 2<sup>6</sup>| 1 * 2<sup>5</sup>| 0 * 2<sup>4</sup> | 1 * 2<sup>3</sup> | 0 * 2<sup>2</sup> | 0 * 2<sup>1</sup> | 1 * 2<sup>0</sup>|
 
 2. Il faut regarder si la portée a été modifiée grâce à cette représentation.
  
  
  **Solution:** 
  
  1. Il faut ajouter 1 au complément à 1 de -113<sub>10</sub>. C'est à dire faire plus 1 à la colonne de 2<sup>0</sup>.
  
  | 2<sup>7</sup> | 2<sup>6</sup> | 2<sup>5</sup> | 2<sup>4</sup> | 2<sup>3</sup> | 2<sup>2</sup> | 2<sup>1</sup> | 2<sup>0</sup> |
  | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
  | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |
  
  2. Il n'y a plus qu'une représentation possible pour (-0)<sub>10</sub>. Il y'a donc un nombre de plus possible par rapport aux dernières représentations. La      nouvelle portée est donc: portée = [-128<sub>10</sub>,+127<sub>10</sub>] 
  
 **Question 5: Floating point ( 10 minutes)**
  
  Voici la représentation en binaire d'un nombre réel:
  
  | Signe | Exposant | Mantisse |
  | --------- | --------- | --------- | 
  | 0 | 10110101 | 01000001000000000000001 |
  
  Que vaut en base 10 la représentation précédente en utilisant la représentation floating point ? Arrondir les résultats intermédiaires et la valeur finale au 3ème chiffre significatif après la virgule.
  
  **Hint:** 
  * Se référer à la diapositive 14 de la semaine 3 pour plus de détails.
  
  * Poser chaque calcul, et ensuite tout fusionner avec la formule. 
  
  * L'exposant et la mantisse sont des entiers positif, donc non signé.
  
  
  **Solution:**
  
  *signe* = 0 --> (-1)<sup>sign</sup> = (-1)<sup>0</sup> = 1
  
  *e* = exposant =  1 * 2<sup>7</sup> + 0 * 2<sup>6</sup> + 1 * 2<sup>5</sup> + 1 * 2<sup>4</sup> + 0 * 2<sup>3</sup> + 1 * 2<sup>2</sup> + 0 * 2<sup>1</sup> + 1 * 2<sup>0</sup> = 181
  
  *2<sup>e-127</sup>* = 2<sup>181-127</sup> = 2<sup>54</sup>
  
  mantisse = 01000001000000000000001 = 1 + 0 * 2<sup>-1</sup> + 1 * 2<sup>-2</sup> + 0 * 2<sup>-3</sup> + (...) + 1 * 2<sup>-8</sup> + 1 * 2<sup>-23</sup> = 1.254
  
  Donc Valeur = (+1) * 1.254 * 2<sup>54</sup> = 2.259 * 10<sup>16</sup>
  
 **Question 6: Conversion d'un nombre binaire au format complément à 2 ( 5 minutes)**
 
   Voici un nombre binaire exprimé sur 8 bits au format complément à 2: (10010011)<sub>2</sub>

   Convertir ce nombre en base 10.

   **Hint:** 
   
   * Utilisez le même tableau que dans les premières questions.
   
   * On applique le processus inverse au complément à deux. C'est à dire faire les opérations sur le nombre binaire dans le sens inverse que dans les questions 3 et 4.

   **Solution:**
   
   Il faut appliquer le processus inverse qu'à la question 3 et 4. Cela permet d'obtenir la valeur positive en binaire du nombre que l'on cherche. Puis il faut convertir cette valeur en base 10 et enfin prendre son inverse.
   
   | Opération | 2<sup>7</sup> | 2<sup>6</sup> | 2<sup>5</sup> | 2<sup>4</sup> | 2<sup>3</sup> | 2<sup>2</sup> | 2<sup>1</sup> | 2<sup>0</sup> |
   | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
   | Aucune| 1 | 0 | 0 | 1 | 0 | 0 | 1 | 1 |
   | Soustraction | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
   | Opposition | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1 |
   
   01101101 = 1 + 4 + 8 + 32 + 64 = (109)<sub>10</sub>
   
   Le nombre est donc (-109)<sub>10</sub>
 
## Exercice 2: Conditions ( 10 minutes)

  Le but de cet exercice est d'entrainer la lecture de code, la compréhension des opérateurs booléens ainsi que le "case switching" à travers le branchement conditionnel.
  
  **Question 1: Branchement conditionnel en java (5 minutes)**
  
   Qu'affiche le code suivant ?
   
   Rappel: Le code suivant est en Java
   
  ```Java
    int numero_mois = 7
    
    switch(numero_mois) {
      
        case 1:
                  System.out.println("Janvier")
                  break;
        case 2:
                  System.out.println("Février")
                  break;
        case 3:
                  System.out.println("Mars")
                  break;
        case 4:
                  System.out.println("Avril")
                  break;
        case 5:
                  System.out.println("Mai")
                  break;
        case 6:
                  System.out.println("Juin")
                  break;
        case 7:
                  System.out.println("Juillet")
                  numero_mois = 9 
        case 8:
                  System.out.println("Août")
                  break;
        case 9:
                  if (numero_mois == 8){
                    System.out.println("Septembre")
                    break;
                    }
                   else{
                     System.out.println("Décembre")
                     numero_mois = 13
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
                  System.out.println("Ce n'est pas un mois. ")
   }
```
  **Hint:** 
  
  1. Break indique que l'on sort de l'accolade. Les cas suivants ne seront pas traités. 
  
  2. Lorsque l'on pose "case n" où n est un nombre cela est équivalent au test n == numero_mois. Ce test est aussi valable si on cherche a comparer des chaînes de caractères ( par exemple si numero_mois = " Juin", à ce moment là n sera aussi une chaîne de caractères).
  
  **Solution:**
  
  Le code va donc afficher:
  
  Juillet 
  Décembre 
  
 __Explication:__ 
  
  1. Comme la case 7 ne contient pas de break et modifie numero_mois, la lecture du code va continuer.
  
  2. On rentre dans le case 9, qui contient un break. Le numero_mois sera aussi modifié mais cela ne sera pas important car on sort de l'accolade et les cas succédants ne seront pas traités.
  
  **Question 2: Conditionnal branching in python (5 minutes)**
  
  Qu'affiche le code suivant ?
  
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
  **Hint:** 
  
  1. Il faut vérifier la condition de chaque cas de manière linéaire.
  
  2. Une fois une condition vérifiée, toutes celles d'après ne sont pas traitées.
  
  **Solution:**
  Le code affiche:
  
  Teacher Algorithmique et pensée computationelle.
  
  
  **Explication**:
  Ci-dessous, le résultat des propositions booléennes des if et elif:
  
  1. (False or False) and True = False 
  
  2. (False and True) or False = False 
  
  3. (False or True) and ( True and False) = True and False = False
  
  4. ((True or True) and True) or ( True and True) = True
