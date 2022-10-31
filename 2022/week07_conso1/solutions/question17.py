sizeX = int(input("Définissez le nombre de ligne que le tableau va faire :"))
sizeY = int(input("Définissez le nombre de colonne que le tableau va faire :"))

# On va sélectionner une case en rentrant ces coordonnées
valueX = int(input("Entrez une line à sélectionner : "))
valueY = int(input("Entrez une case à sélectionner : "))

#print Header
for h in range(0,(sizeY*2)+2):
    print("-", end="")

#Print the line
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
            print("- ",end = '')

    #print the element of the line
    print("|")

#print Footer
for f in range(0,(sizeY*2)+2):
    print("-", end="")