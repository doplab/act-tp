abstract class Figure {

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

    @Override
    public float getperimetre() {
        return this.largeur * 4;
    }

    @Override
    public float getaire() {
        return this.largeur * this.largeur;
    }

}

class Rectangle extends Figure {

    public Rectangle (float largeur, float longueur){
        super(largeur, longueur);
    }

    @Override
    public float getperimetre(){
        return (this.largeur + this.longueur)*2;

    }
    @Override
    public float getaire(){
        return this.largeur * this.longueur;
    }
}

public class Main {
    public static void main(String[] args) {
        Carre c = new Carre(5.0f);
        Rectangle r = new Rectangle(4.0f, 3.0f);

        System.out.println(c.getperimetre());
        System.out.println(r.getaire());
    }
}