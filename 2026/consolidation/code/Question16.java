import java.util.List;

public class Question16 {

    public static int nb_voyelles_iterative(String S, List L) {
        // TODO
    }

    public static int nb_voyelles_recursive(String S, List L) {
        // TODO
    }

    public static void main(String[] args) {
        List voyelles = List.of('a', 'e', 'i', 'o', 'u', 'y');
        String texte = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean molestie elit ipsum, a tincidunt urna aliquet";

        System.out.println(nb_voyelles_iterative(texte, voyelles));
        System.out.println(nb_voyelles_recursive(texte, voyelles));
    }
}
