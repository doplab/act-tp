l = ["Schmitt", True, "Irma", False, "Khalif", True, "Yasser", False, "Wang", True]
dict_final = {}
i = 0                                 # Variable qui permettra d'itérer et de gérer la boucle while.
while i < len(l):                     # La boucle s'arrêtera donc au bout de 10 itérations. La valeur maximale de i sera 9.
	if i % 2 == 0:                    
            dict_final[l[i]] = l[i + 1]
        i +=1                             # On incrémente i  