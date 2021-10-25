age = int(input("Veuillez entrer l'age de la personne : "))
if age < 21 :
    print("Entrée : Pas OK")
else :
    if age>25 :
        print("Entrée : OK, Boisson : Pas OK")
    else :
        print("Entrée : OK, Boisson : OK")