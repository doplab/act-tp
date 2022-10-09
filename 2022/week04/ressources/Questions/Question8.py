value1 = "Algorithms"
value2 = 4


try:
    decimal = float(value2)
except ValueError as error:
    print("Nous ne pouvons pas convertir un entier en décimal")

finally:
    try:
        value2 = int(value1)
    except ValueError as error:
        print("Nous ne pouvons pas convertir une chaîne de caractères en nombre")
