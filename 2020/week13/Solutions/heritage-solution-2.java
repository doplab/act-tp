
public class Livre_Audio extends Livre {
    private String narrateur;

    public Livre_Audio(String titre, String auteur, int annee, String narrateur){
        super(titre, auteur, annee);
        System.out.println("Création d'un livre audio");
        this.narrateur = narrateur;
    }

    // redéfinition de la fonction printInfo() dans la sous-classe Book
    public void printInfo() {
        super.printInfo(); //permet de reprendre les éléments de la fonction mère
        System.out.println("Narrateur: "+ narrateur); //On ajoute l attribut supplémentaire propre à la sous-classe
    }
}

