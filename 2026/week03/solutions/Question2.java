import java.util.Scanner;

public class Question2 {
    public static void main(String[] args) {
        Scanner myScanner = new Scanner(System.in);

        System.out.println("Entrez votre Prenom : ");
        String prenom = myScanner.nextLine();

        System.out.println("Entrez votre Nom : ");
        String nom = myScanner.nextLine();
        System.out.println("Bonjour, " + prenom + " " + nom);
    }
}
