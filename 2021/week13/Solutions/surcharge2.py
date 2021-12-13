    # Question 8
    def add(self, f):
        self.__num = self.__num * f.__den + f.__num * self.__den
        self.__den = self.__den * f.__den
        self.simplification()

    def plus(self, f):
        q = Fraction(self.__num, self.__den)
        q.add(f)
        return q

    def __add__(self, other):
        if isinstance(other, Fraction):
            return self.plus(other)
        elif isinstance(other, int):
            self.add__ = self.__add__(Fraction(other))
            return self.add__
        else:
            raise TypeError(
                "Unsupported operand types for +: '" + self.__class__.__name__ + "' and '" + other.__class__.__name__ + "'")

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.__num * other.__num, self.__den * other.__den)
        elif isinstance(other, int):
            return Fraction(self.__num * other, self.__den)
        # On affiche un message d'erreur lorsque other n'est pas une Fraction
        else:
            raise TypeError(
                "Unsupported operand types for *: '" + self.__class__.__name__ + "' and '" + other.__class__.__name__ + "'")

if __name__ == '__main__':
    f1 = Fraction()
    print(f1)
    f1 = Fraction(4)
    print(f1)
    f1 = Fraction(denominateur=5)
    print(f1)
    f1 = Fraction(4, -6)
    print(f1)
    f2 = Fraction(2, -8)
    print(f2)
    print(f1+f2)
    print(f1 == Fraction(22, -24))
    print(f1 == Fraction(1, 2))
