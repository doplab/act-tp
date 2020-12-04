public class Livre {

    private String titre;
    private String auteur;
    private int annee;
    private int note = -1;

    public Livre(String titre, String auteur, int annee){
        System.out.println("Création d'un livre");
        this.titre = titre;
        this.auteur = auteur;
        this.annee = annee;
    }

    public void printInfo() {
        System.out.println("A propos du livre");
        System.out.println("------------------");
        System.out.println("Titre : \""+titre+"\"");
        System.out.println("Auteur : "+auteur);
        System.out.println("Année : "+annee);
        System.out.println("Note : "+note);
    }

    public void setNote(int note) {
        this.note = note;
    }
}

public class Livre_Audio extends Livre {
    private String narrateur;

    public Livre_Audio(String titre, String auteur, int annee, String narrateur){
        super(titre, auteur, annee);
        System.out.println("Création d'un livre audio");
        this.narrateur = narrateur;
    }
}

public class Livre_Illustre extends Livre {

    private String dessinateur;

    public Livre_Illustre(String titre, String auteur, int annee, String dessinateur) {
        super(titre, auteur, annee);
        System.out.println("Création d'un livre illustré");
        this.dessinateur = dessinateur;
    }
}
