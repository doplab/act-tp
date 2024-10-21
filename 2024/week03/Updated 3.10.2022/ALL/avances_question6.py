# Programme écrit en Python
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
