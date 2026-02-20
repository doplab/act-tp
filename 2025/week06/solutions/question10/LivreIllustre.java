class LivreIllustre extends Livre {

    private String illustrateur;

    public LivreIllustre(String titre, String auteur, int annee, String illustrateur) {
    super(titre, auteur, annee);
    System.out.println("Création d'un livre illustré");
    this.illustrateur = illustrateur;
    }
}