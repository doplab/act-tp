from random import randint
number = randint(0, 30)
for i in range(5):
    x = int(input("Choississez un nombre: "))
    if x==number:
        print("Yeah!")
        break
    elif x<number:
        print("Trop petit!")
    else:
        print("Trop grand!")