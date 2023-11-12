package com.company;

class Attaquant extends Fighter {

    private int multiplicateur;

    public Attaquant(String name, int health, int attack, int defense, int multiplicateur) {
        super(name, health, attack, defense);
        this.multiplicateur = multiplicateur;
    }

    public int getMultiplicateur() {
        return multiplicateur;
    }

    public void setMultiplicateur(int multiplicateur) {
        this.multiplicateur = multiplicateur;
    }

    public void attack(String type, Fighter other) {
        for (int i = 0; i < this.getMultiplicateur(); i++) {
            System.out.println("Attaque n " + (i+1));
            super.attack(type, other);
        }
    }

}