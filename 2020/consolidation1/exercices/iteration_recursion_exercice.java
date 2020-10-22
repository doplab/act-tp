import java.util.List;

public class Main {

    public static int nb_voyelles_itérative(String S, List L){
        //TODO
    }

    public static int nb_voyelles_récursive(String S, List L){
        //TODO
    }
    public static void main(String[] args) {
        List voyelles = List.of('a','e','i','o','u','y');
        String texte = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean molestie elit ipsum, a tincidunt urna aliquet" +
                " eget. Praesent et quam vitae justo hendrerit tristique. Ut malesuada ligula in mi ultricies tempor. Fusce blandit" +
                " turpis sapien, in gravida orci aliquet et. Morbi in metus efficitur, volutpat purus sit amet, scelerisque massa." +
                " Vivamus vehicula justo quis leo feugiat fringilla. Maecenas sagittis ultrices accumsan. Cras libero est, gravida in" +
                "  eros ac, luctus ullamcorper nisi.";

        System.out.println(nb_voyelles_itérative(texte, voyelles));
        System.out.println(nb_voyelles_récursive(texte, voyelles));
        }
    }
