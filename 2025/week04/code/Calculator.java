import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Entrez le premier entier: ");
        double num1 = sc.nextInt();

        System.out.print("Entrez le deuxième entier: ");
        double num2 = sc.nextInt();

        System.out.print("Entrez l'opération (+, -, *, /): ");
        char op = sc.next().charAt(0);

        sc.close();

        switch (op) {
            case '+':
                System.out.println(num1 + num2);
            case '-':
                System.out.println(num1 - num2);
            case '*':
                System.out.println(num1 * num2);
            case '/':
                System.out.println(num1 / num2);
            default:
                throw new IllegalArgumentException("L'opération n'est pas valide");
        }
    }
}
