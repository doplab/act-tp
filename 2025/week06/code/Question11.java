public class Question11 {

    public static void main(String[] args) {
        Livre Livre1 = new Livre_Audio("Hamlet", "Shakespeare", 1609,"William");
        Livre1.setNote(5);
        Livre Livre2 = new Livre("Les Misérables","Hugo",1862);
        System.out.print(Livre1);
        System.out.print(Livre2);
    }
}