class Carre extends Figure {

    public Carre(double largeur) {
        super(largeur, largeur);
    }

    @Override
    public double getPerimetre() {
        return this.largeur * 4;
    }

    @Override
    public double getAire() {
        return this.largeur * this.largeur;
    }

}