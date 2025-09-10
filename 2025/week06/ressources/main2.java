public class Main {
    public static void main(String[] args) {
        Fighter P1 = new Fighter("P1", 10, 2, 2);
        Fighter P2 = new Fighter("P2", 10, 2, 2);
        Fighter P3 =  new Fighter("P3", 10, 2, 2);
        P1.attack("pied",P2);
        P1.attack("poing",P2);
        P1.attack("tete",P2);
        P1.attack("tete",P2);
    }
}
