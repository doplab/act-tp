public abstract class Figure {

    protected float largeur;
    protected float longueur;

    public Figure(float largeur, float longueur){
        this.largeur = largeur;
        this.longueur = longueur;
    }

    public abstract float getperimetre();
    public abstract float getaire();
}

class Carre extends Figure {

    public Carre(float largeur) {
        super(largeur, largeur);
    }

    public float getperimetre(float largeur) {
        return largeur + largeur;
    }

    public float getaire(float largeur) {
        return largeur * largeur;
    }
}

class Rectangle extends Figure {

    public Rectangle (float largeur, float longueur){
        super(largeur, longueur);
    }
    public float getperimetre(float largeur, float longueur){
        return largeur + longueur;

    }
    public float getaire(float largeur, float longueur){
        return largeur * longueur;
    }
}