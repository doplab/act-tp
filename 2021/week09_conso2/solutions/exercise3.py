def nombresImpairs(limite):
    for nb in range(limite+1):
        if nb % 2 == 1:
            print(nb)

limit = int(input("Entrez une valeur maximale: "))

print("Nombres impairs compris entre 1 et " + str(limit) + " : ")
nombresImpairs(limit)
