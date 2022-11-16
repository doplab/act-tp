public class Fraction {
    private int numerateur;
    private int denominateur;

    public Fraction(int numerateur, int denominateur){
        this.numerateur = numerateur;
        this.denominateur = denominateur;
        simplify();
    }

    public int gcd(int a, int b){
        if (a==0){
            return b;
        } else if (b==0) {
            return a;
        } else{
            return gcd(b%a, a);
        }
    }

    private void simplify(){
        int pgcd = gcd(this.numerateur, this.denominateur);
        this.numerateur = this.numerateur / pgcd;
        this.denominateur = this.denominateur / pgcd;
    }

    @Override
    public String toString() {
        return numerateur + "/" + denominateur;
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) return true;
        if (other == null || this.getClass() != other.getClass()) return false;
        return this.numerateur * ((Fraction) other).denominateur == ((Fraction) other).numerateur * this.denominateur;
    }
}
