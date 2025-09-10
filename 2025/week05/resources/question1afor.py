l = ["Schmitt", True, "Irma", False, "Khalif", True, "Yasser", False, "Wang", True]
dict_final = {}
for i in range(len(l)):               # i va de 0 à 9
	if i % 2 == 0:                    # Test si i est pair. Si oui, on crée une nouvelle entrée dans le dictionnaire
		dict_final[l[i]] = l[i + 1]   