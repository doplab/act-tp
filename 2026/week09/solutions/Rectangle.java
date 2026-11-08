class Rectangle extends Figure {

    public Rectangle(double largeur, double longueur) {
        super(largeur, longueur);
    }

    @Override
    public double getPerimetre() {
        return (this.largeur + this.longueur) * 2;

    }

    @Override
    public double getAire() {
        return this.largeur * this.longueur;
    }
}