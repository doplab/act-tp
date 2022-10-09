value1 = "Algorithms"
value2 = 4

try:
    size = len(value1)
    result = size/value2
    print(f"Le résultat de la division est: {result}")

except Exception as error:
    print("On ne peut pas effectuer l'opération")

try:
    result = value1/2
    print(f"Le résultat de la division est: {result}")
    
except TypeError as error:
    print("On ne peut pas diviser une chaine de caractère")
