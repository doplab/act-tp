public class Question4 {
    public static void main(String[] args) {
        Fighter p1 = new Fighter("P1", 10, 2, 2);
        Fighter p2 = new Fighter("P2", 10, 2, 2);
        Fighter p3 =  new Fighter("P3", 10, 2, 2);
        p1.attack("pied",p2);
        p1.attack("poing",p2);
        p1.attack("tete",p2);
        p1.attack("tete",p2);
    }
}
