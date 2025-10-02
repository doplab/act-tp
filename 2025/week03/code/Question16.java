public class Question16 {
    public static void main(String[] args) {
        String s = "UNIL\nSchool of Criminal Sciences";

        System.out.println(s); // \n crée un saut de ligne

        // Imprimer uniquement la sous-chaîne School of crimi.
        System.out.println(s.substring(5, 20));

        // Accéder au troisième caractère
        System.out.println(s.charAt(2)); // 'h'

        System.out.println(s.length());
    }
}
