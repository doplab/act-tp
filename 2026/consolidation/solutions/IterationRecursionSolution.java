import java.util.List;

public class IterationRecursionSolution {

    public static int nb_voyelles_iterative(String text) {
        List<Character> voyelles = List.of('a', 'e', 'i', 'o', 'u', 'y');
        int c = 0;
        for (int i = 0; i < text.length(); i++) {
            if (voyelles.contains(text.charAt(i))) {
                c++;
            }
        }
        return c;
    }

    public static int nb_voyelles_recursive(String text) {
        List<Character> voyelles = List.of('a', 'e', 'i', 'o', 'u', 'y');
        if (text.isEmpty()) {
            return 0;
        } else {
            if (voyelles.contains(text.charAt(0))) {
                return 1 + nb_voyelles_recursive(text.substring(1, text.length()));
            } else {
                return 0 + nb_voyelles_recursive(text.substring(1, text.length()));
            }
        }
    }

    public static void main(String[] args) {
        String text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean molestie elit ipsum, a tincidunt urna aliquet"
                +
                " eget. Praesent et quam vitae justo hendrerit tristique. Ut malesuada ligula in mi ultricies tempor. Fusce blandit"
                +
                " turpis sapien, in gravida orci aliquet et. Morbi in metus efficitur, volutpat purus sit amet, scelerisque massa."
                +
                " Vivamus vehicula justo quis leo feugiat fringilla. Maecenas sagittis ultrices accumsan. Cras libero est, gravida in"
                +
                "  eros ac, luctus ullamcorper nisi.";

        System.out.println(nb_voyelles_iterative(text));
        System.out.println(nb_voyelles_recursive(text));
    }
}
