import java.util.Scanner;

public class Question13 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String step = scanner.nextLine();
        switch (step) {
            case "fetch":
                System.out.println("L'étape fetch s'exécute ou va être exécutée.");
            case "decode":
                System.out.println("L'étape decode s'exécute ou va être exécutée.");
            case "execute":
                System.out.println("L'étape execute s'exécute ou va être exécutée.");
            case "store":
                System.out.println("L'étape store s'exécute ou va être exécutée.");
                break;
            default:
                System.out.println("L'étape n'est pas valide");
        }
    }
}