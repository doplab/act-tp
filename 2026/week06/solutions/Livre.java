public class Livre {

    private String titre;
    private String auteur;
    private int annee;
    private int note = -1;

    public Livre(String titre, String auteur, int annee){
    System.out.println("Création d'un livre");
    this.titre = titre;
    this.auteur = auteur;
    this.annee = annee;
}

public int getNote(){
    return this.note;
}

public void setNote(int note) {
    this.note = note;
}

public String toString() {
    if (note == -1){
        return "A propos du livre \n------------------ \nTitre : " +titre+ "\nAuteur : "+auteur+ "\nAnnée : "+annee+ "\nNote : non attribuée";
        }
    else{
        return "A propos du livre \n------------------ \nTitre : " +titre+ "\nAuteur : "+auteur+ "\nAnnée : "+annee+ "\nNote : "+note;
        }
    }
}

