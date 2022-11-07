class Livre_Audio extends Livre {

    private String narrateur;

    public Livre_Audio(String titre, String auteur, int annee, String narrateur){
        super(titre, auteur, annee);
        System.out.println("Création d'un livre audio");
        this.narrateur = narrateur;
}

    // redéfinition de la fonction toString dans la classe fille Livre_Audio
    public String toString() {
        return super.toString() + "\nNarrateur: "+ narrateur+"\n"; //Ajoute narrateur à la chaine de caractère crée par la classe mère (super)
    }
}

class Livre_Illustre extends Livre {

    private String illustrateur;

    public Livre_Illustre(String titre, String auteur, int annee, String illustrateur) {
        super(titre, auteur, annee);
        System.out.println("Création d'un livre illustré");
        this.illustrateur = illustrateur;
}
    public String toString() {
        return super.toString() + "\nIllustrateur: "+ illustrateur + "\n"; //Ajoute illustrateur à la chaine de caractère crée par la classe mère (super)
    }
}