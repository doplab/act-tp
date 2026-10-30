class Carre extends Figure {

    public Carre(float largeur) {
        super(largeur, largeur);
    }

    @Override
    public float getPerimetre() {
        return this.largeur * 4;
    }

    @Override
    public float getAire() {
        return this.largeur * this.largeur;
    }

}