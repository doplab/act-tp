import java.util.ArrayList;

public class Joueur {

    private Carte[] hand;
    private int balance;
    private boolean monTour;
    private String nom;


    public Joueur(Carte c1, Carte c2, int initialeBalance, String nom){
        hand = new Carte[2];
        hand[0] = c1;
        hand[1] = c2;
        monTour = false;
        balance = initialeBalance;
        this.nom = nom;
    }


    public void montrerMain(){
        for (int i = 0; i < hand.length; i++){
            hand[i].getInfo();
        }
    }

    public void miser(int valeur ){
        if (monTour && balance-valeur > 0 ){
            balance -= valeur;
            System.out.println("Le joueur " + nom + " vient de miser: " + Integer.toString(valeur));
            System.out.println("La nouvelle Balance: "+  Integer.toString(balance));

        } else {
            System.out.println("Pas assez d'argent!");
        }
    }

    public void gagner(int valeur){
        if (monTour) {
            this.balance += valeur;

        }
    }
}

