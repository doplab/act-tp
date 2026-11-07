public class Fraction {
    private int numerateur;
    private int denominateur;

    public Fraction(int numerateur, int denominateur) {
        this.numerateur = numerateur;
        if (denominateur == 0) {
            throw new ArithmeticException();
        }
        // alternative (aux lignes 7 à 9)
        // var tmp = numerateur / denominateur;
        this.denominateur = denominateur;
        simplify();
    }

    public static int gcd(int a, int b) {
        if (a == 0) {
            return b;
        } else if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }

    private void simplify() {
        int pgcd = Fraction.gcd(this.numerateur, this.denominateur);
        this.numerateur = this.numerateur / pgcd;
        this.denominateur = this.denominateur / pgcd;
    }

    @Override
    public String toString() {
        return numerateur + "/" + denominateur;
    }

    @Override
    public boolean equals(Object other) {
        if (this == other)
            return true;
        if (other == null || this.getClass() != other.getClass())
            return false;
        Fraction f = (Fraction) other;
        return this.numerateur * f.denominateur == f.numerateur * this.denominateur;
    }
}
