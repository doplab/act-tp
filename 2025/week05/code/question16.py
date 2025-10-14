bool_test = True

while bool_test:
    # Tant que bool_test est True, la boucle continue
    test_value = int(input("Veuillez entrer un entier : "))

    # On veut sortir de la boucle si test_value est 10
    # Pour sortir, il faut que bool_test soit False
    # D'où l'utilisation de not qui transforme True en False et vice versa
    bool_test = not(test_value == 10)

    if bool_test:
        print("Ce n'est pas le bon entier.")

print("Bravo !")