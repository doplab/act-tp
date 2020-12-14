public class Guerrier extends Personnage {
    
    public Guerrier(String nom, int niveau, int pv,  int vitalite, int force, int dexterite, int endurance, int intelligence) {
        super(nom,  niveau, pv, vitalite,  force,  dexterite,  endurance,  intelligence);

    }
    public void attaqueBasique(Personnage other){
        int attaque = (int) (getForce()*0.5);

        other.setPv(other.getVitalite()-attaque);

        System.out.println(this.getNom() + " attaque " + other.getNom());
        System.out.println("Basic attaque og : " + attaque);
        System.out.println(this.getNom() + " PV:" + this.getPv());
        System.out.println(other.getNom() + " PV:" + this.getPv());

    }
}

public class Magicien extends Personnage {


    public Magicien(String nom, int niveau, int pv, int vitalite, int force, int dexterite, int endurance, int intelligence) {
        super(nom,  niveau, pv, vitalite,  force,  dexterite,  endurance,  intelligence);
    }
    @Override
    public void attaqueBasique(Personnage other){
        int attaque = (int) (getIntelligence()*0.5);

        other.setPv(other.getVitalite()-attaque);

        System.out.println(this.getNom() + " attaque " + other.getNom());
        System.out.println("Basic attaque og : " + attaque);
        System.out.println(this.getNom() + " PV:" + this.getPv());
        System.out.println(other.getNom() + " PV:" + this.getPv());

    }

}

public class Paladin extends Personnage {

    public Paladin(String nom, int niveau, int pv, int vitalite, int force, int dexterite, int endurance, int intelligence) {
        super(nom,  niveau, pv,  vitalite,  force,  dexterite,  endurance,  intelligence);
    }


    @Override
    public void attaqueBasique(Personnage other){
        int attaque = (int) (getEndurance()*0.7);

        other.setPv(other.getVitalite()-attaque);

        System.out.println(this.getNom() + " attaque " + other.getNom());
        System.out.println("Basic attaque og : " + attaque);
        System.out.println(this.getNom() + " PV:" + this.getPv());
        System.out.println(other.getNom() + " PV:" + this.getPv());

    }
}


public class Chasseur extends Personnage {

    public Chasseur(String nom, int niveau, int pv, int vitalite, int force, int dexterite, int endurance, int intelligence) {
        super(nom,  niveau, pv,  vitalite,  force,  dexterite,  endurance,  intelligence);
    }

    @Override
    public void attaqueBasique(Personnage other){
        int attaque = (int) (getDexterite()*0.5);

        other.setPv(other.getVitalite()-attaque);

        System.out.println(this.getNom() + " attaque " + other.getNom());
        System.out.println("Basic attaque og : " + attaque);
        System.out.println(this.getNom() + " PV:" + this.getPv());
        System.out.println(other.getNom() + " PV:" + this.getPv());

    }
}

