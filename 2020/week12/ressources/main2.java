public class Main {

    public static void main(String[] args) {
        Fighter P1 = new Fighter("P1", 50, 30, 10);
        Fighter P2 = new Fighter("P2", 50, 25, 10);
        Fighter P3 =  new Fighter("P3", 50, 25, 10);
        P1.attack(P2);
        P1.attack(P2);
        P1.attack(P2);
        P1.attack(P2);
    }
}