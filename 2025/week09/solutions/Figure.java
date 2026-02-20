public abstract class Figure {

    protected float largeur;
    protected float longueur;

    public Figure(float largeur, float longueur) {
        this.largeur = largeur;
        this.longueur = longueur;
    }

    public abstract float getPerimetre();

    public abstract float getAire();
}