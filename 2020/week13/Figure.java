package com.company;

public abstract class Figure {

    public abstract float getperimetre();
    public abstract float getaire();
    }

public class Carre extends Figure {
    private float cote;

    public Carre(float c) {
        cote = c;
    }

    public float getperimetre(float cote) {
        return cote + cote;
    }

    public float getaire(float cote) {
        return cote * cote;
    }
}

public class Rectangle extends Figure {
    private float largeur;
    private float longueur;

    public Rectangle (float lar, float lon){
        largeur = lar;
        longueur = lon;
    }
    public float getpertimetre(float largeur, float longueur){
        return largeur + longueur;

    }
    public float getaire(float largeur, float longueur){
        return largeur * longueur;
    }
}
