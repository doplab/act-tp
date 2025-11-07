public class Main {
    public static void main(String[] args) {
        Fraction f1 = new Fraction(8, 32);
        Fraction f2 = new Fraction(1, 4);
        System.out.println(f1==f2);
        System.out.println(f1.equals(f2));
    }
}