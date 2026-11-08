public abstract class Personnage {

    private String nom;
    private int niveau;
    private int pv;

    private int vitalite;
    private int force;
    private int dexterite;
    private int endurance;
    private int intelligence;


    public Personnage(String nom, int niveau, int pv, int vitalite,
                      int force, int dexterite, int endurance, int intelligence) {
        this.nom = nom;
        this.niveau = niveau;
        this.pv = pv;

        this.vitalite = vitalite;
        this.force = force;
        this.dexterite = dexterite;
        this.endurance = endurance;
        this.intelligence = intelligence;

    }

    @Override
    public String toString() {
        return "Nom : " + nom + ", niveau : " + niveau
            + ", PV : " + pv + ", vitalite : " + vitalite
            + ", force : " + force + ", dexterite : " + dexterite
            + ", endurance : " + endurance
            + ", intelligence : " + intelligence;
    }


    public abstract void attaqueBasique(Personnage autre);

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
        if (pv > 0) {
            this.pv = pv;
        }
        else {
            this.pv = 0;
        }
    }
}
