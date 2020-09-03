Algorithmes et Pensée Computationnelle
======================================

# Programmation de base

Le but de cette séance est d'aborder des notions de base en programmation. Au terme de cette séance, l'étudiant sera capable de:
- définir une variable, de définir son type et sa valeur.
- Définir une fonction et comprendre son rôle.
- Utiliser des notions d'algèbre booléenne.
- Comprendre la notion d'entrée/sortie.
Les langages qui seront utilisés pour cette séance sont __Java__ et __Python__. Assurez-vous d'avoir bien installé __Pycharm__ et __Netbeans__. Si vous rencontrez des difficultés, n'hésitez pas à vous référer au guide suivant: ** tutoriel d'installation des outils et prise en main de l'environnement de travail **.


## Représentation de nombres entier

**Question 1: Unsigned int** 

Sur 8 bit écrire 113 en base binaire.

**Hint:** Faire un tableau comme présenté dans le cours page 9 de la semaine 3. Essayer de décomposer en une somme de puissances de 2 le nombre.

**Solution:** 
1. Décomposer le nombre en une somme de puissances de 2.

113 = 64 + 32 + 16 + 1 = 1 * 2^6 + 1 * 2^5 + 1* 2^4 + 1 * 2^0

2.  Inclure les coefficients dans un tableau:

| 2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 |
| --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 |

Donc la représentation en binaire de l'entier non signé 113 est: 01110001



