class Livre_Illustre extends Livre {

    private String illustrateur;

    public Livre_Illustre(String titre, String auteur, int annee, String illustrateur) {
    super(titre, auteur, annee);
    System.out.println("Création d'un livre illustré");
    this.illustrateur = illustrateur;
    }
}