bool_test = True
while bool_test:                                          # Tant que bool_test est True, la boucle continue
	test_value = int(input("Veuillez entrer un entier"))  # Pour que le test effectué à la ligne suivante ne soit pas toujours juste                         
                                                                #  ( comparaison entre un string et un entier), il faut changer le type de l'input.
	bool_test = not(test_value == 10)                     # On veut sortir de la boucle si la test_value est 10. Pour sortir il faut que bool_test soit  
     	if bool_test == True:                                 # False. D'où l'utilisation de not qui transforme true en false et vice verse.
        	print("Ce n'est pas le bon entier.")              
print("Bravo !")