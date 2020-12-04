public class Main {
    public static void main(String[] args) {
        Combattant P1 = new Combattant("P1", 10, 2, 2);
        Attaquant P2 = new Attaquant("P2", 10, 2, 2,2);
        Soigneur P3 = new Soigneur("P3",10,4,2,4);
        P1.attack("pied",P2);
        P1.attack("poing",P2);
        P1.attack("tete",P2);
        P1.attack("tete",P2);
        P3.résurrection(P2);
        P1.attack("pied",P2);
        P1.attack("poing",P2);
        P1.attack("tete",P2);
        P3.attack(P2);
        P2.attack("tete",P1);
    }
}