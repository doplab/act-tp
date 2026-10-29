sizeX = int(input("Définissez le nombre de lignes que le tableau va faire :"))
sizeY = int(input("Définissez le nombre de colonnes que le tableau va faire :"))

# On va sélectionner une case en rentrant ces coordonnées
valueX = int(input("Entrez une line à sélectionner : "))
valueY = int(input("Entrez une case à sélectionner : "))

# Iterate over the lines 
for x in range(0,sizeX):
    if x == (valueX-1) and valueY == 0 :
        print("")
        print("X", end = '')
    else:
        print("")
        print("|", end = '')

    #print the column
    for y in range (0,sizeY):
        if x == (valueX-1) and y == (valueY-1):
            print("X ", end='')
            #print the basic element
        else:
            print("- ", end = '')

    #Iterate over the columns
    print("|")