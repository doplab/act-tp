import java.util.Scanner;

public class Question2 {
    public static void main(String[] args) {
        Scanner my_scanner = new Scanner(System.in);

        System.out.println("Entrez votre Prenom : ");
        String prenom = my_scanner.nextLine();

        System.out.println("Entrez votre Nom : ");
        String nom = my_scanner.nextLine();
        System.out.println("Bonjour, " + prenom + " " + nom);
    }
}
