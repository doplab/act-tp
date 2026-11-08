public class Magicien extends Personnage {
    public Magicien(String nom, int niveau, int pv, int vitalite,
                    int force, int dexterite, int endurance, int intelligence) {
        super(nom, niveau, pv, vitalite, force, dexterite, endurance, intelligence);
    }

    @Override
    public void attaqueBasique(Personnage autre) {
        int degats = (int) (getIntelligence() * 0.5);
        autre.setPv(autre.getPv() - degats);

        System.out.println(getNom() + " attaque " + autre.getNom());
        System.out.println(autre.getNom() + " : " + autre.getPv() + " PV restants");
    }
}
