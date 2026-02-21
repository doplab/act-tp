from random import randint

if __name__ == "__main__":
    number = randint(0, 30)

    for i in range(3):
        x = int(input("Choississez un nombre: "))
        if x==number: # l'utilisateur a deviné le nombre choisi aléatoirement par l'ordi
            print("Yeah!")
            break  # cette instruction nous permet de sortir de la bouble
        elif x<number:
            print("Trop petit!")
        else:
            print("Trop grand!")