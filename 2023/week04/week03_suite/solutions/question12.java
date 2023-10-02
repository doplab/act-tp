public class Main {
    public static void main(String[] args) {
        int numero_mois = 7;

        switch(numero_mois) {

            case 1:
                System.out.println("Janvier");
                break;
            case 2:
                System.out.println("Février");
                break;
            case 3:
                System.out.println("Mars");
                break;
            case 4:
                System.out.println("Avril");
                break;
            case 5:
                System.out.println("Mai");
                break;
            case 6:
                System.out.println("Juin");
                break;
            case 7:
                System.out.println("Juillet");
                numero_mois = 9 ;
            case 8:
                System.out.println("Aout");
            case 9:
                if (numero_mois == 8){
                    System.out.println("Septembre");
                    break;
                }
                else{
                    System.out.println("Décembre");
                    numero_mois = 13;
                    break;
                }
            case 10:
                System.out.println("Octobre");
                break;
            case 11:
                System.out.println("Novembre");
                break;
            case 12:
                System.out.println("Décembre");
                break;
            default:
                System.out.println("Ce n'est pas un mois. ");
        }
    }
}