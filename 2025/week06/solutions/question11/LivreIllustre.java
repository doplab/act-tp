class LivreIllustre extends Livre {

    private String illustrateur;

    public LivreIllustre(String titre, String auteur, int annee, String illustrateur) {
        super(titre, auteur, annee);
        System.out.println("Création d'un livre illustré");
        this.illustrateur = illustrateur;
    }

    public String toString() {
        return super.toString() + "\nIllustrateur: " + illustrateur + "\n"; // Ajoute illustrateur à la chaine de
                                                                            // caractère crée par la classe mère (super)
    }
}