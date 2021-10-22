import math


# Question 1: Création de la classe Fraction
class Fraction:
    # Question 2: Déclaration du constructeur et initialisation des valeurs
    def __init__(self, numerateur=0, denominateur=1):
        # Question 3: type casting
        self.__num = int(numerateur)
        self.__den = int(denominateur)
        self.simplification()

    # Question 4: redéfinition de la méthode __str__()
    def __str__(self):
        return "Votre fraction a pour valeur {}/{}".format(self.__num, self.__den)

    # Question 5: Getters et Setters
    def get_num(self):
        return self.__num

    def get_den(self):
        return self.__den

    def set_num(self, n):
        self.__num = n

    def set_den(self, d):
        d = int(d)
        # Si on passe 0 au dénominateur, on lève une exception ce qui arrêtera le programme
        if d == 0:
            raise ZeroDivisionError
        self.__den = d

    # Question 6
    def simplification(self):
        if self.__num == 0:
            self.__den = 1
        if self.__den < 0:
            self.__num = -self.__num
            self.__den = -self.__den
        pgcd = math.gcd(self.__num, self.__den)
        self.__num = int(self.__num / pgcd)
        self.__den = int(self.__den / pgcd)

    # Question 7
    def __eq__(self, f):
        if isinstance(f, Fraction):
            # vu que les fractions sont toujours en représentation simplifiée, on pourrait se contenter de
            # self.__numerateur == f.__numerateur and self.__denominateur = f.denominateur
            return self.__num * f.__den == f.__num * self.__den
        # Au cas où on reçoit un seul argument, on créé une fraction ayant pour numérateur l'argument et 1 comme dénominateur
        elif isinstance(f, int):
            return self.__eq__(Fraction(f))
        else:
            return False

    # Question 8
    def add(self, f):
        self.__num = self.__num * f.__den + f.__num * self.__den
        self.__den = self.__den * f.__den
        self.simplification()

    def plus(self, f):
        q = Fraction(self.__num, self.__den)
        q.add(f)
        return q
