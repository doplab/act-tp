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