public class Main {
    public static void main(String[] args) {
        Combattant P1 = new Combattant("P1", 10, 2, 2);
        Combattant P2 = new Combattant("P2", 10, 2, 2);
        Combattant P3 =  new Combattant("P3", 10, 2, 2);
        P1.attack("pied",P2);
        P1.attack("poing",P2);
        P1.attack("tete",P2);
        P1.attack("tete",P2);
    }
}
