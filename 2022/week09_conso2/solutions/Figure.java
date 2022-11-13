abstract class Figure {

    protected float largeur;
    protected float longueur;

    public Figure(float largeur, float longueur){
        this.largeur = largeur;
        this.longueur = longueur;
    }

    public abstract float getPerimetre();
    public abstract float getAire();
}

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

class Rectangle extends Figure {

    public Rectangle (float largeur, float longueur){
        super(largeur, longueur);
    }

    @Override
    public float getPerimetre(){
        return (this.largeur + this.longueur)*2;

    }
    @Override
    public float getAire(){
        return this.largeur * this.longueur;
    }
}

public class Main {
    public static void main(String[] args) {
        Carre c = new Carre(5.0f);
        Rectangle r = new Rectangle(4.0f, 3.0f);

        System.out.println(c.getPerimetre());
        System.out.println(r.getAire());
    }
}