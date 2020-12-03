public class Main {
    public static void main(String[] args) {
        Combattant P1 = new Combattant("P1", 10, 2, 2);
        Combattant P2 = new Attaquant("P2", 10, 2, 2);
        Combattant P3 =  new Attaquant("P3", 10, 2, 3);
        P1.attack("pied",P2);
        P1.attack("poing",P2);
        P1.attack("tete",P2);
        P1.attack("tete",P2);
        Soigneur P4 = new Soigneur("P4",10,2,2,4);
        P4.résurection(P2);
        P1.attack("pied",P4);
        P1.attack("poing",P4);
        P1.attack("tete",P4);
        P1.attack("tete",P4);
        P4.résurection(P2);
        Soigneur P5 = new Soigneur("P5",10,2,2,4);
        P5.soigne(P4);
        P2.attack("tete",P2);
    }
}