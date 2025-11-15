public class Carte {

    private int valeur;
    private int couleur;

    public static final int HEART = 0;
    public static final int DIAMOND = 1;
    public static final int SPADE = 2;
    public static final int CLUB = 3;


    public Carte(int valeur, int couleur){
        this.valeur = valeur;
        this.couleur = couleur;
    }

    public void getInfo(){
        System.out.println("Carte: " + getValeur() + " de " + getCouleur());
    }

    public String getValeur() {
        String res = "";
        switch (valeur) {
            case 11:
                res = "Valet";
                break;
            case 12:
                res = "Dame";
                break;
            case 13:
                res = "King";
                break;
            default:
                res = Integer.toString(valeur);
                break;

        }
        return res;
    }

    public String getCouleur() {
        String res = "";
        switch (couleur) {
            case 0:
                res = "Coeur";
                break;
            case 1:
                res = "Carreau";
                break;
            case 2:
                res = "Pic";
                break;
            default:
                res = "Trèfle";
                break;

        }
        return res;
    }
}
