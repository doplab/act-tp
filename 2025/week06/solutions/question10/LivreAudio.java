class LivreAudio extends Livre {
    private String narrateur;

    public LivreAudio(String titre, String auteur, int annee, String narrateur){
    super(titre, auteur, annee);
    System.out.println("Création d'un livre audio");
    this.narrateur = narrateur;
    }
}