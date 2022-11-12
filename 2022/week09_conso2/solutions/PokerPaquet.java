import java.util.ArrayList;
import java.util.Random;

public class Paquet {

    private ArrayList<Carte>  paquet;
    public static final int NBR_CARTES = 52;
    public static final int NBR_MELANGES = 100;

    public Paquet(){
        this.paquet = new ArrayList<>();

        for ( int couleur = Carte.HEART; couleur <= Carte.CLUB; couleur++ ) {
            for (int valeur = 1; valeur <= 13; valeur++) {
                paquet.add(new Carte(valeur, couleur));
            }
        }
        melanger();
    }


    public void melanger(){
        int index_1, index_2;

        Random generator = new Random();
        Carte temp;

        for (int i=0; i<NBR_MELANGES; i++) {
            index_1 = generator.nextInt( paquet.size() - 1 );
            index_2 = generator.nextInt( paquet.size() - 1 );
            temp = paquet.get( index_2 );
            paquet.set( index_2 , paquet.get( index_1 ) );
            paquet.set( index_1, temp );

        }

    }


    public Carte getCarte(){
        return paquet.remove(0);
    }


}
