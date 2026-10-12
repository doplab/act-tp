public class Question11 {

    public static void main(String[] args) {
        Livre livre1 = new LivreAudio("Hamlet", "Shakespeare", 1609,"William");
        livre1.setNote(5);
        Livre livre2 = new Livre("Les Misérables","Hugo",1862);
        System.out.print(livre1);
        System.out.print(livre2);
    }
}
