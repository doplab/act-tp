public class Main {

    public static void main(String[] args) {
    Livre Livre1 = new Livre_Audio("Hamlet", "Shakespeare", 1609,"William");
    Livre1.setNote(5);
    System.out.println(Livre1);
    Livre Livre2 = new Livre("Les Misérables","Hugo",1862);
    System.out.println(Livre2);

}

}