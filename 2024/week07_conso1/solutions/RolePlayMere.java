import java.util.Random;

public class Personnage {

    private String nom;
    private int niveau;
    private int pv;

    private int vitalite;
    private int force;
    private int dexterite;
    private int endurance;
    private int intelligence;


    public Personnage(String nom, int niveau, int pv, int vitalite, int force, int dexterite, int endurance, int intelligence){
        this.nom = nom;
        this.niveau = niveau;
        this.pv = pv;

        this.vitalite = vitalite;
        this.force = force;
        this.dexterite = dexterite;
        this.endurance = endurance;
        this.intelligence = intelligence;

    }

    public void getInfo() {
        System.out.println("Nom" + getNom());
        System.out.println("Niveau" + getNiveau());
        System.out.println("Vitalité" + getVitalite());
        System.out.println("Force" + getForce());
        System.out.println("Dexterité" + getDexterite());
        System.out.println("Endurance" + getEndurance());
        System.out.println("Intelligence" + getIntelligence());
    }


    public void attaqueBasique(Personnage other){
        System.out.println(this.getNom() + " attaque " + other.getNom());
    }

    public String getNom() {
        return nom;
    }

    public int getIntelligence() {
        return intelligence;
    }

    public int getNiveau() {
        return niveau;
    }

    public int getPv() {
        return pv;
    }

    public int getVitalite() {
        return vitalite;
    }

    public int getForce() {
        return force;
    }

    public int getDexterite() {
        return dexterite;
    }

    public int getEndurance() {
        return endurance;
    }

    public void setPv(int pv) {
        if (pv > 0){
            this.pv = pv;
        }
        else{
            this.pv = 0;
        }
    }
}