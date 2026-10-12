class LivreAudio extends Livre {
    private String narrateur;

    public LivreAudio(String titre, String auteur, int annee, String narrateur){
    super(titre, auteur, annee);
    this.narrateur = narrateur;
    }
}
