# Question 8
    def __add__(self, other):
    if isinstance(other, int):
        other = Fraction(other)

    if isinstance(other, Fraction):
        result = Fraction(
            self.__num * other.__den + other.__num * self.__den,
            self.__den * other.__den
        )
        result.simplification()
        return result

    print(
        f"Unsupported operand types for +: "
        f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
    )

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.__num * other.__num, self.__den * other.__den)
        elif isinstance(other, int):
            return Fraction(self.__num * other, self.__den)
        # On affiche un message d'erreur lorsque other n'est pas une Fraction
        else:
            print("Unsupported operand types for *: '" + self.__class__.__name__ + "' and '" + other.__class__.__name__ + "'")

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
    f1=Fraction(numerateur=5, denominateur=0)
    print(f1)