import java.util.List;

public class Question16 {

    public static int nbVoyellesIterative(String texte, List voyelles) {
        // TODO
    }

    public static int nbVoyellesRecursive(String texte, List voyelles) {
        // TODO
    }

    public static void main(String[] args) {
        List voyelles = List.of('a', 'e', 'i', 'o', 'u', 'y');
        String texte = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean molestie elit ipsum, a tincidunt urna aliquet";

        System.out.println(nbVoyellesIterative(texte, voyelles));
        System.out.println(nbVoyellesRecursive(texte, voyelles));
    }
}
