public class Question22 {
    public static void main(String[] args) {
        // Essayez d'exécuter avec un argument de la ligne de commande
        System.out.println(getBinaryRepresentation(args[0]));
    }

    public static String getBinaryRepresentation(String arg) {
        int a = Integer.parseInt(arg);
        if (a == 0) {
            return "";
        }
        int b = a / 2;
        int r = a % 2;
        return getBinaryRepresentation(String.valueOf(b)) + String.valueOf(r);
    }
}