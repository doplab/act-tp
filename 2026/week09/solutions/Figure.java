public abstract class Figure {

    protected double largeur;
    protected double longueur;

    public Figure(double largeur, double longueur) {
        this.largeur = largeur;
        this.longueur = longueur;
    }

    public abstract double getPerimetre();

    public abstract double getAire();
}