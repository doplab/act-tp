public class Question11 {

    public static void main(String[] args) {
        Livre livreAudio = new LivreAudio("Hamlet", "Shakespeare", 1609, "William");
        livreAudio.setNote(5);
        Livre livreIllustre = new LivreIllustre("Les Misérables", "Victor Hugo", 1862, "Gustave Brion");

        System.out.println(livreAudio);
        System.out.println(livreIllustre);
    }
}
