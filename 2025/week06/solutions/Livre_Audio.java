class Livre_Audio extends Livre {
    private String narrateur;

    public Livre_Audio(String titre, String auteur, int annee, String narrateur){
    super(titre, auteur, annee);
    System.out.println("Création d'un livre audio");
    this.narrateur = narrateur;
    }
}