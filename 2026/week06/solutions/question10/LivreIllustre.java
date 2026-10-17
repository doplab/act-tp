class LivreIllustre extends Livre {

    private String illustrateur;

    public LivreIllustre(String titre, String auteur, int annee, String illustrateur) {
    super(titre, auteur, annee);
    this.illustrateur = illustrateur;
    }
}
