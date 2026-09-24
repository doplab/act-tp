from random import randint

number = randint(0, 30)

# Première chance pour deviner le nombre
x = int(input("Choississez un nombre: "))
if x==number:
    print("Yeah!")
elif x<number:
    print("Trop petit!")
else:
    print("Trop grand!")

# Deuxième chance pour deviner le nombre
x = int(input("Choississez un nombre: "))
if x==number:
    print("Yeah!")
elif x<number:
    print("Trop petit!")
else:
    print("Trop grand!")

# Troisième chance pour deviner le nombre
x = int(input("Choississez un nombre: "))
if x==number:
    print("Yeah!")
elif x<number:
    print("Trop petit!")
else:
    print("Trop grand!")