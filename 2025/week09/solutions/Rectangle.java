class Rectangle extends Figure {

    public Rectangle(float largeur, float longueur) {
        super(largeur, longueur);
    }

    @Override
    public float getPerimetre() {
        return (this.largeur + this.longueur) * 2;

    }

    @Override
    public float getAire() {
        return this.largeur * this.longueur;
    }
}