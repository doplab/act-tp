package com.company;

class Soigneur extends Fighter {

    private int résurrection;

    public Soigneur(String name, int health, int attack, int defense, int soin){
        super(name,health,attack,defense);
        résurrection = 1;
    }

    public int getRésurrection(){
        return this.résurrection;
    }

    public void setRésurrection(int etat){
        this.résurrection = etat;
    }

    public void résurrection(Fighter other){
        if(!this.isAlive()) {
            System.out.println(this.getName() + " est mort et ne peut plus rien faire");
        }
        else{
            if (other.isAlive()) {
                System.out.println(other.getName() + " est toujours en vie !");
            } else {
                if (this.getRésurrection() == 0) {
                    System.out.println(this.getName() + " ne peut plus ressuciter personne");
                } else {
                    other.setHealth(10);
                    Fighter.addInstances(other);
                    this.setRésurrection(0);
                    System.out.println(other.getName() + " vient de revenir à la vie");
                    Fighter.checkHealth();
                }
            }
        }
    }

    public void attack(Fighter other) {
        if(!this.isAlive()) {
            System.out.println(this.getName() + " est mort et ne peut plus rien faire");
        }
        else{
            if (other.getHealth() >= 10) {
                System.out.println(other.getName() + " a déjà le maximum de points de vie");
            }
            if (!other.isAlive()) {
                System.out.println(other.getName() + " est déjà mort, ressuscitez-le pour pouvoir le soigner");
            } else {
                other.setHealth(other.getHealth() + this.getAttack());
                Fighter.checkHealth();
            }
        }
    }

}